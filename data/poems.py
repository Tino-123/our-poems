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
#                this once it has been revealed.
# reveal_date:   "YYYY-MM-DD" -- the date this entry unlocks.
# title:         shown as the heading, e.g. "August" or "For You".
# banner:        OPTIONAL. Big centered text shown first, before the
#                title (e.g. "HAPPY BIRTHDAY"). Leave out entirely for a
#                normal month with no banner.
# poem:          your poem text, triple-quoted so line breaks are kept.
# images:        list of paths to image files in the images/ folder.
# reveal_delays: OPTIONAL. Only affects the newest (most recent) poem --
#                that's the only one that gets the staged reveal.
#                Format: [banner_delay_ms, title_delay_ms, body_delay_ms]
#                -- each is measured from page load, not from the
#                previous stage. Body = the full poem text + photos,
#                which all appear together (nothing is staged further
#                after that). Defaults to [800, 3000, 6500] if omitted.
# -----------------------------------------------------------------------

POEMS = [
    {
        "id": "2026-08-birthday",
        "reveal_date": "2026-08-07",
        "title": "For You",
        "banner": "HAPPY BIRTHDAY",
        "poem": """In the beginning, the earth was without form, and void;
and darkness was upon the face of the deep.
And God said, Let there be light: and there was light.

In the language of the universe,
Spark and Word were the first things that precede the universe
Spark, when the silence first cracked open into the most beautiful explosion of light,
Word, when God breathed, and the dark gave way to light, the nothingness to the meaningful

you came like that first spark,
quiet, slowly spreading, taking space, chasing the darkness,
I contributed to give my life a meaning and life
when I thought I was condemned to boredom

God in his magnificence, underneath any of his creation
has hidden a melody
a melody driven by a rhythm,
a melody driven by his breath,
a melody driven by love.

And underneath you, I found a song,
the melody of an unconditional love,
the notes of elegance and
the rhythm of beauty

When I sometimes think about the attributes that make us human,
I often think about the smile
smile for me is,
the simplest signature of mankind.
Maybe that's the reason why I love to see you smile — happy.

Today,
A new spark has been ignited,
The stars, as witnesses, have aligned on this day in your honor,
forming the constellation of Lyra, chanting your name
New words are being pronounced,
Words of blessings,
health, prosperity, ……

Today,
A new chapter,
New experiences, new feelings, knowledges
Makes this new chapter worth it and

Remember,
God has already provided the foundation, the terrain,
Now whatever you become is in your hand,
If not then take control back over your life and live as you truly wish

Remember,
In the moments of difficulty, doubt, remember what you are standing on,
Remember the cornerstone supporting you,
Remember that it's unbreakable,
And hold on to your faith,
Keep in mind where you are coming from and where you wanna go

I will be there, supporting, cheering, you alongside the ones who truly wish to love you or perhaps who love you

Now go enjoy your day,
go conquer your world and be happy

Happy Birthday""",
        "images": [
            "images/image-1.jpeg",
            "images/image-2.jpeg",
             "images/image-3.jpeg",
             "images/image-4.jpeg",
             "images/image-5.jpeg",
             "images/image-6.jpeg",
             "images/image-7.jpeg",
             "images/image-8.jpeg",
             "images/image-9.jpeg",
             "images/image-10.jpeg",
        ],
        "reveal_delays": [800, 3000, 6500],
    },
]
