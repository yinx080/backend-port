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
PORTRAIT_ALT = "Portrait photo"


# ---------------------------------------------------------------------------
# HEADLINE
# ---------------------------------------------------------------------------
NAME = "Your Name"
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
    {"label": "Shooting since", "value": "20XX"},
    {"label": "Languages", "value": "Spanish, English"},
    {"label": "Travels for work", "value": "Yes, anywhere"},
    {"label": "Availability", "value": "Booking now"},
]


# ---------------------------------------------------------------------------
# WHAT I SHOOT - cards
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "title": "Nightlife",
        "description": "Club nights and events cut to the music. One sentence on "
                       "what you deliver and how fast.",
    },
    {
        "title": "Automotive",
        "description": "Rolling shots, static features, car meets. Say what you "
                       "bring to it.",
    },
    {
        "title": "Music Video",
        "description": "Concept to final grade. Mention whether you handle the "
                       "treatment too.",
    },
    {
        "title": "Brand & Social",
        "description": "Short-form verticals for Instagram and TikTok. Mention "
                       "turnaround and how many cuts they get.",
    },
]


# ---------------------------------------------------------------------------
# GEAR - grouped lists. Set GEAR = [] to hide the whole section.
# ---------------------------------------------------------------------------
GEAR = [
    {"category": "Cameras", "items": ["Body one", "Body two"]},
    {"category": "Lenses", "items": ["Lens one", "Lens two", "Lens three"]},
    {"category": "Movement", "items": ["Gimbal", "Drone"]},
    {"category": "Light & Sound", "items": ["Light one", "Mic one"]},
    {"category": "Post", "items": ["Editing software", "Grading tool"]},
]


# ---------------------------------------------------------------------------
# LINKS - shown as a row of buttons
# ---------------------------------------------------------------------------
SOCIALS = [
    {"label": "Instagram", "url": "https://instagram.com/your-handle"},
    {"label": "YouTube", "url": "https://youtube.com/@your-handle"},
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
