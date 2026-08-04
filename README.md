# Monthly Poems

A private website + email that reveals one poem (with photos) per month,
automatically. You write poems by editing one Python file and pushing to
GitHub -- everything else (revealing on the site, sending the email) runs
by itself on a schedule.

## How it works

- `data/poems.py` holds every entry: a title, poem text, images, and the
  date it should unlock (`reveal_date`).
- `build.py` generates a static website (`site/`) containing only the
  entries whose `reveal_date` has passed.
- `send_email.py` emails any entry that just unlocked and hasn't been
  emailed yet (it keeps track in `sent_log.json` so nothing repeats).
- A GitHub Actions workflow (`.github/workflows/deploy.yml`) runs both of
  these **every day automatically**, and publishes the site to GitHub
  Pages. You don't run or host anything yourself.

## One-time setup (about 15 minutes)

### 1. Create a GitHub repository
- Go to github.com, create a **new repository** (can be private or public
  -- note: GitHub Pages on a *private* repo requires a paid GitHub plan;
  if you want it fully private and free, see the "Keeping it private"
  note below).
- Upload all the files in this project to that repository (drag-and-drop
  works fine on github.com, or use `git push` if you're comfortable with
  git).

### 2. Turn on GitHub Pages
- In the repo, go to **Settings → Pages**.
- Under "Build and deployment", set **Source** to **GitHub Actions**.

### 3. Set up an email sender
The easiest option is a Gmail account with an **App Password**:
1. Turn on 2-Step Verification on the Gmail account (Google Account →
   Security).
2. Go to Google Account → Security → **App passwords**, create one
   (choose "Mail" as the app), and copy the 16-character password.

### 4. Add secrets to GitHub
In the repo, go to **Settings → Secrets and variables → Actions → New
repository secret**, and add each of these:

| Secret name  | Value                                  |
|--------------|-----------------------------------------|
| `SMTP_SERVER`| `smtp.gmail.com`                        |
| `SMTP_PORT`  | `587`                                   |
| `EMAIL_USER` | your Gmail address                      |
| `EMAIL_PASS` | the 16-character app password from step 3|
| `RECIPIENT`  | the email address of the person you're sending poems to |

(Using a different email provider is fine too -- just use its SMTP
settings instead.)

### 5. Trigger the first run
- Go to the **Actions** tab in your repo → select the "Build, Email, and
  Deploy" workflow → **Run workflow** (this triggers it manually the
  first time; after that it also runs automatically every day at 08:00
  UTC).
- Once it finishes, your site will be live at:
  `https://<your-username>.github.io/<repo-name>/`

## Adding a new month

1. Open `data/poems.py`.
2. Add a new entry to the `POEMS` list, e.g.:

   ```python
   {
       "id": "2026-09",
       "reveal_date": "2026-09-01",
       "title": "September",
       "poem": """Your poem
       goes here,
       line by line.""",
       "images": ["images/sept-1.jpg", "images/sept-2.jpg"],
   },
   ```
3. Put the actual image files in the `images/` folder, named to match
   (e.g. `images/sept-1.jpg`).
4. Commit and push (or upload via github.com).

You can add several months ahead of time -- each one only appears on the
site and gets emailed once its `reveal_date` arrives. The `id` should be
unique and never reused.

## Testing locally (optional)

If you have Python installed:

```bash
python build.py       # builds site/index.html -- open it in a browser
python send_email.py  # requires the env vars above to be set locally
```

## Keeping it private

- A **private GitHub repo** keeps your poems.py source hidden, but a free
  GitHub Pages site is still reachable by anyone with the exact URL
  (it's just not indexed or linked anywhere). For most personal gifts
  this "unlisted" privacy is enough.
- For real access-control (password-protected site), you'd need a paid
  Pages plan or a different host (e.g. Netlify with password protection).
  Ask me if you'd like this set up instead.

## Changing the look

Edit `build_assets/style.css` for colors/fonts, and the `SITE_TITLE` /
`SITE_SUBTITLE` variables near the top of `build.py` for the page text.
