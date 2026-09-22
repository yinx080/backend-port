import logging
import re
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import about  # all the text on the /about page lives in about.py
import inquiries  # sends the contact form on to your inbox
import rates  # packages and form options for the /rates page
from models import InquiryRequest

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("portfolio")

# Load .env when running locally. On Railway the variables are already in the
# environment, and python-dotenv may not be installed there - either is fine.
try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent / ".env")
except ImportError:
    pass

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://portfolio-frontend-production-ae40.up.railway.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
UPLOADS_DIR = BASE_DIR / "uploads"
COMPRESSED_DIR = UPLOADS_DIR / "compressed"
ABOUT_DIR = UPLOADS_DIR / "about"

# Bump this whenever you replace a video/thumbnail/poster WITHOUT renaming it.
# It changes every ?v= in the API responses, so browsers fetch the new files
# instead of serving the cached ones.
VERSION = 3

DEFAULT_ASPECT = 16 / 9


class CachedStatic(StaticFiles):
    """StaticFiles + long-lived cache headers (files are versioned via ?v=)."""

    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if response.status_code in (200, 206, 304):
            response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        return response


# Serves everything inside uploads/, including uploads/compressed/.
# Handles Range requests (video seeking, Safari) and fails at startup if
# the folder is missing, so you'll see it in the Railway deploy logs.
app.mount("/media", CachedStatic(directory=UPLOADS_DIR), name="media")


def jpeg_size(path: Path):
    """Return (width, height) of a JPEG by reading only its header, or None."""
    try:
        with open(path, "rb") as f:
            if f.read(2) != b"\xff\xd8":
                return None
            while True:
                byte = f.read(1)
                if not byte:
                    return None
                if byte != b"\xff":
                    continue
                marker = f.read(1)
                while marker == b"\xff":  # skip fill bytes
                    marker = f.read(1)
                if not marker:
                    return None
                m = marker[0]
                if m == 0x00 or m == 0x01 or 0xD0 <= m <= 0xD8:  # no length field
                    continue
                if m == 0xD9:  # end of image, no size found
                    return None
                length = int.from_bytes(f.read(2), "big")
                # Start-of-frame markers hold the image dimensions
                if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                    f.read(1)  # sample precision
                    height = int.from_bytes(f.read(2), "big")
                    width = int.from_bytes(f.read(2), "big")
                    return width, height
                f.seek(length - 2, 1)
    except OSError:
        return None


def aspect_of(name: str) -> float:
    """
    Aspect ratio (width / height) of a video, read automatically from its
    poster. The poster is generated from the video by ffmpeg, so it has the
    same ratio. Falls back to 16:9 if the poster is missing or unreadable.
    """
    size = jpeg_size(COMPRESSED_DIR / f"{name}_poster.jpg")
    if size and size[0] > 0 and size[1] > 0:
        return round(size[0] / size[1], 4)
    return round(DEFAULT_ASPECT, 4)


def project(id: int, title: str, filename: str, category: str = "Nightlife / Videography"):
    name = Path(filename).stem
    return {
        "id": id,
        "title": title,
        "category": category,
        "video_url": f"/media/{filename}?v={VERSION}",
        "thumb_url": f"/media/compressed/{name}_thumb.mp4?v={VERSION}",
        "poster_url": f"/media/compressed/{name}_poster.jpg?v={VERSION}",
        "aspect": aspect_of(name),
    }


PROJECTS = [
    project(2, "Narnya", "narnya2.mp4"),
    project(1, "Narnya 2", "test-edit.mp4"),
    project(3, "Narnya 3", "narnya3.mp4"),
    project(4, "Pangea", "pangea5.mp4"),
    project(5, "Pangea 2", "pangea2.mp4"),
    project(6, "Pangea 3", "pangea3.mp4"),
    project(7, "Pangea 4", "pangea4.mp4"),
    project(8, "Pangea 5", "16_2.mp4"),
    project(9, "Rumours Tibu", "rumourstibu1.mp4"),
    project(10, "Rumours Tibu 2", "rumourstibu2.mp4"),
]


@app.get("/api/projects")
def get_projects():
    return PROJECTS


# --- ABOUT PAGE ------------------------------------------------------------
# The content itself is in about.py. This just wraps it for the frontend and
# resolves the portrait to a URL (or None, if the file isn't there yet).


def portrait_url():
    """URL for the about-page photo, or None if it hasn't been added yet."""
    filename = getattr(about, "PORTRAIT", None)
    if not filename:
        return None
    if not (ABOUT_DIR / filename).is_file():
        return None
    return f"/media/about/{filename}?v={VERSION}"


@app.get("/api/about")
def get_about():
    return {
        "name": about.NAME,
        "role": about.ROLE,
        "location": about.LOCATION,
        "portrait_url": portrait_url(),
        "portrait_alt": about.PORTRAIT_ALT,
        "bio": about.BIO,
        "facts": about.FACTS,
        "services": about.SERVICES,
        "gear": about.GEAR,
        "socials": about.SOCIALS,
        "cta": about.CTA,
    }


# --- INQUIRIES PAGE --------------------------------------------------------
# Packages and copy come from rates.py. Submissions go through inquiries.py.


@app.get("/api/rates")
def get_rates():
    return {
        "heading": rates.HEADING,
        "intro": rates.INTRO,
        "packages": rates.PACKAGES,
        "price_note": rates.PRICE_NOTE,
        "custom": rates.CUSTOM,
        "budgets": rates.BUDGETS,
        "response_time": rates.RESPONSE_TIME,
        "fallback_email": rates.FALLBACK_EMAIL,
    }


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s.]+\.[^@\s]+$")


# Deliberately NOT async: inquiries.send_inquiry does a blocking HTTP call, so
# FastAPI runs this whole function in a worker thread and the rest of the API
# keeps serving while an email is on its way.
@app.post("/api/inquiries")
def create_inquiry(inquiry: InquiryRequest):
    # Spam trap: bots fill the hidden field, humans never see it. Answer as if
    # it worked, so the bot has nothing to learn, and drop it.
    if inquiry.website:
        log.info("Dropped a honeypot submission")
        return {"ok": True, "delivered": False}

    if not EMAIL_PATTERN.match(inquiry.email.strip()):
        return {"ok": False, "error": "That email address doesn't look right."}

    data = inquiry.model_dump(exclude={"website"})

    # Logged before anything else, so an email failure never loses the message.
    log.info("NEW INQUIRY: %s", data)

    delivered = inquiries.send_inquiry(data)
    return {"ok": True, "delivered": delivered}