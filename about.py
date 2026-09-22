"""
EVERYTHING THE "ABOUT" PAGE SAYS LIVES IN THIS FILE.

You should never have to touch React to change this page. Edit the values
below, restart the backend, refresh the page.

How it behaves:
  * Every list can be reordered, extended, or emptied. Setting a list to []
    makes that whole section disappear from the page - no layout holes.
  * PORTRAIT points at a file inside  uploads/about/.  Until that file
    exists the page shows a labelled empty frame instead of a broken image.
  * After you REPLACE a photo without renaming it, bump VERSION in main.py
    so browsers fetch the new one instead of the cached one.

Placeholder text below is written as instructions to yourself - swap it for
the real thing whenever you're ready.
"""

# ---------------------------------------------------------------------------
# THE PHOTO
# ---------------------------------------------------------------------------
# Filename only. The file itself goes in:  uploads/about/<PORTRAIT>
# A portrait-orientation shot works best - the frame on the page is 4:5.
PORTRAIT = "portrait.jpg"

# Shown to screen readers and if the image ever fails to load.
PORTRAIT_ALT = "Holding a Sony Handycam camcorder on a rig with a light"


# ---------------------------------------------------------------------------
# HEADLINE
# ---------------------------------------------------------------------------
NAME = "Ignacio Almonte Santos"
ROLE = "Videographer & Editor"
LOCATION = "Málaga, Spain"


# ---------------------------------------------------------------------------
# BIO - one string per paragraph
# ---------------------------------------------------------------------------
BIO = [
    "First paragraph: who you are and what you do. Two or three sentences is "
    "plenty. Say where you're based, what kind of work you shoot, and how long "
    "you've been doing it.",

    "Second paragraph: how you work. What a shoot with you feels like, what you "
    "care about in an edit, the kind of look you chase. This is the part people "
    "actually read before they email you.",

    "Third paragraph (optional - delete this line if you don't want it): "
    "anything personal that makes you memorable. How you got started, what you "
    "were doing before, what you shoot for fun.",
]


# ---------------------------------------------------------------------------
# QUICK FACTS - small label/value rows under the photo
# ---------------------------------------------------------------------------
FACTS = [
    {"label": "Based in", "value": "Málaga, Spain"},
    {"label": "Shooting since", "value": "2026"},
    {"label": "Languages", "value": "Spanish, English"},
    {"label": "Travels for work", "value": "Yes, anywhere"},
    {"label": "Availability", "value": "Booking now"},
]


# ---------------------------------------------------------------------------
# WHAT I SHOOT - cards
# ---------------------------------------------------------------------------
# "description" is optional: leave it out (or empty) and the card shows just
# the title. Add a sentence whenever you feel like it.
SERVICES = [
    {
        "title": "Nightlife",
        "description": "Club nights and events cut to the music.",
    },
    {
        "title": "Automotive",
        "description": "Rolling shots, static features, car meets.",
    },
    {
        "title": "Brand & Social",
        "description": "Short-form verticals for Instagram and TikTok.",
    },
]


# ---------------------------------------------------------------------------
# GEAR - grouped lists.
# ---------------------------------------------------------------------------
# Empty for now, so the "Kit" section doesn't render at all. When you want it
# back, fill it in using the shape shown underneath:
#
#   GEAR = [
#       {"category": "Cameras", "items": ["Sony Handycam", "..."]},
#       {"category": "Lenses", "items": ["...", "..."]},
#       {"category": "Movement", "items": ["Gimbal", "Drone"]},
#       {"category": "Light & Sound", "items": ["...", "..."]},
#       {"category": "Post", "items": ["...", "..."]},
#   ]
GEAR = []


# ---------------------------------------------------------------------------
# LINKS - shown as a row of buttons
# ---------------------------------------------------------------------------
SOCIALS = [
    {"label": "Instagram", "url": "https://www.instagram.com/cameraboy.vhs/"},
    {"label": "YouTube", "url": "https://www.youtube.com/@That_Boi_Saint"},
    {"label": "Email", "url": "mailto:you@example.com"},
]


# ---------------------------------------------------------------------------
# CALL TO ACTION at the bottom of the page
# ---------------------------------------------------------------------------
# "href" starting with "/" is treated as an internal route, anything else
# opens in a new tab. Set CTA = None to hide it.
CTA = {
    "heading": "Got something to shoot?",
    "text": "One line inviting them to reach out. Keep it short and direct.",
    "label": "Work with me",
    "href": "/rates",
}
