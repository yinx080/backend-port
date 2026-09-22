"""
EVERYTHING ON THE INQUIRIES PAGE LIVES IN THIS FILE.

Same deal as about.py: edit here, restart, refresh. Prices are strings, so
"€350", "From €350" and "Ask me" all work.

Emptying a list hides its section. Removing "includes" from a package just
drops the bullet list from that card.
"""

HEADING = "Inquiries"
INTRO = "Packages below. Anything that doesn't fit one, tell me what you have in mind."


# ---------------------------------------------------------------------------
# PACKAGES - the cards at the top of the page
# ---------------------------------------------------------------------------
# "highlight": True draws one card brighter than the others. Use it on the one
# you actually want people to pick, or on none of them.
PACKAGES = [
    {
        "name": "Reel",
        "price": "From €XXX",
        "summary": "One short-form vertical edit.",
        "includes": [
            "Up to X hours shooting",
            "One edit, up to XX seconds",
            "X round of changes",
            "Delivered in X days",
        ],
        "highlight": False,
    },
    {
        "name": "Event Night",
        "price": "From €XXX",
        "summary": "Full coverage of a night, cut to the music.",
        "includes": [
            "Up to X hours on site",
            "One main edit plus X clips for stories",
            "X rounds of changes",
            "Delivered in X days",
        ],
        "highlight": True,
    },
    {
        "name": "Full Production",
        "price": "From €XXX",
        "summary": "Bigger jobs: concept, shoot, grade.",
        "includes": [
            "Full day shooting",
            "Concept and shot planning",
            "Main edit plus cutdowns",
            "Colour grade",
        ],
        "highlight": False,
    },
]


# ---------------------------------------------------------------------------
# THE "SOMETHING ELSE" BLOCK under the packages
# ---------------------------------------------------------------------------
# Set CUSTOM = None to remove it.
CUSTOM = {
    "title": "Something else in mind?",
    "text": "If none of these fit, tell me the idea and I'll quote it.",
    "label": "Custom project",  # what lands in the form's "package" field
}


# ---------------------------------------------------------------------------
# FORM OPTIONS
# ---------------------------------------------------------------------------
# Budget dropdown. Set BUDGETS = [] to drop the field entirely.
BUDGETS = [
    "Under €300",
    "€300 - €600",
    "€600 - €1200",
    "€1200+",
    "Not sure yet",
]

# Shown under the form and on the thank-you screen.
RESPONSE_TIME = "I usually reply within 24 hours."

# Fallback shown if the form fails to send, so nobody leaves without a way
# to reach you. Keep this the same address you actually read.
FALLBACK_EMAIL = "you@example.com"
