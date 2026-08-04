# -----------------------------------------------------------------------
# THIS IS THE ONLY FILE YOU NORMALLY NEED TO EDIT.
#
# Add one entry to POEMS for each month. As soon as today's date reaches
# "reveal_date", that entry will:
#   - appear on the website (after the next automatic build), and
#   - be emailed automatically (once) to the recipient.
#
# You can add entries for future months ahead of time -- they simply won't
# show up (or be emailed) until their reveal_date arrives.
#
# id:            unique short id, e.g. "2026-08". Never reuse or change
#                this once it has been revealed (it's used to avoid
#                re-sending the same email).
# reveal_date:   "YYYY-MM-DD" -- the date this entry unlocks.
# title:         shown as the heading, e.g. "August".
# poem:          your poem text. Use triple-quoted strings so line breaks
#                are kept exactly as you write them.
# images:        list of paths to image files. Put the actual image files
#                in the images/ folder, and reference them here as
#                "images/whatever.jpg".
# -----------------------------------------------------------------------

POEMS = [
    {
        "id": "2026-08",
        "reveal_date": "2026-08-07",
        "title": "August",
        "poem": """This is for my love""",
        "images": [
            # "images/august-1.jpg",
            # "images/august-2.jpg",
        ],
    },
    # {
    #     "id": "2026-09",
    #     "reveal_date": "2026-09-01",
    #     "title": "September",
    #     "poem": """...""",
    #     "images": ["images/september-1.jpg"],
    # },
]
