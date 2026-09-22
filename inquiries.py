"""
Delivery of contact-form submissions.

Right now that means one email through Resend. Everything is read from the
environment at send time, so you can change it in Railway without a code
change:

    RESEND_API_KEY   your Resend key. Missing = nothing is emailed.
    INQUIRY_TO       the inbox you want the messages in.
    INQUIRY_FROM     verified sender. Defaults to Resend's test sender,
                     which only delivers to your own Resend account email.

Every inquiry is written to the server log before any of this happens, so a
misconfigured key or a Resend outage loses nothing - the message is still in
your Railway logs.

Swapping Resend for something else later means rewriting send_inquiry() and
nothing else.
"""

import json
import logging
import os
import urllib.error
import urllib.request

log = logging.getLogger("inquiries")

RESEND_ENDPOINT = "https://api.resend.com/emails"
DEFAULT_FROM = "onboarding@resend.dev"
TIMEOUT_SECONDS = 15


def _plain_text(inquiry: dict) -> str:
    lines = [
        f"From:    {inquiry.get('name')} <{inquiry.get('email')}>",
        f"Package: {inquiry.get('package') or '-'}",
        f"Budget:  {inquiry.get('budget') or '-'}",
        f"Date:    {inquiry.get('event_date') or '-'}",
        "",
        (inquiry.get("message") or "").strip(),
    ]
    return "\n".join(lines)


def _html(inquiry: dict) -> str:
    def esc(value):
        return (
            str(value or "-")
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    message = esc(inquiry.get("message")).replace("\n", "<br>")
    return (
        "<div style=\"font-family:system-ui,sans-serif;font-size:15px;line-height:1.6\">"
        f"<p><strong>{esc(inquiry.get('name'))}</strong> &lt;{esc(inquiry.get('email'))}&gt;</p>"
        "<table cellpadding='0' cellspacing='0' style='font-size:14px'>"
        f"<tr><td style='padding-right:16px;color:#666'>Package</td><td>{esc(inquiry.get('package'))}</td></tr>"
        f"<tr><td style='padding-right:16px;color:#666'>Budget</td><td>{esc(inquiry.get('budget'))}</td></tr>"
        f"<tr><td style='padding-right:16px;color:#666'>Date</td><td>{esc(inquiry.get('event_date'))}</td></tr>"
        "</table>"
        f"<p style='margin-top:20px;white-space:pre-wrap'>{message}</p>"
        "</div>"
    )


def send_inquiry(inquiry: dict) -> bool:
    """
    Email one inquiry. Returns True if Resend accepted it.

    Never raises: the caller should not fail a visitor's form submission
    because an email provider had a bad minute.
    """
    api_key = os.getenv("RESEND_API_KEY")
    to_address = os.getenv("INQUIRY_TO")
    from_address = os.getenv("INQUIRY_FROM", DEFAULT_FROM)

    if not api_key or not to_address:
        log.warning(
            "Inquiry NOT emailed: set RESEND_API_KEY and INQUIRY_TO to enable "
            "delivery. The inquiry itself is in the log line above."
        )
        return False

    payload = {
        "from": from_address,
        "to": [to_address],
        "subject": f"Inquiry - {inquiry.get('package') or 'Website'} - {inquiry.get('name')}",
        "text": _plain_text(inquiry),
        "html": _html(inquiry),
    }

    # So you can just hit reply and answer the person directly.
    sender = (inquiry.get("email") or "").strip()
    if sender:
        payload["reply_to"] = sender

    request = urllib.request.Request(
        RESEND_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            if 200 <= response.status < 300:
                log.info("Inquiry emailed to %s", to_address)
                return True
            log.error("Resend returned %s", response.status)
            return False
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:500]
        log.error("Resend rejected the email (%s): %s", exc.code, body)
        return False
    except Exception as exc:  # network down, DNS, timeout...
        log.error("Could not reach Resend: %s", exc)
        return False
