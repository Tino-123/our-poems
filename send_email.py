"""
Emails any poem that has been revealed (reveal_date <= today) and hasn't
been emailed yet. Keeps track of what's been sent in sent_log.json so
nothing is ever sent twice.

Needs these environment variables (set as GitHub Actions secrets, see
README.md):
  SMTP_SERVER    e.g. smtp.gmail.com
  SMTP_PORT      e.g. 587
  EMAIL_USER     the sending address
  EMAIL_PASS     an app password (NOT your normal password)
  RECIPIENT      the address to send poems to
"""

import json
import os
import smtplib
from datetime import date
from email.message import EmailMessage
from pathlib import Path

from data.poems import POEMS

ROOT = Path(__file__).parent
LOG_FILE = ROOT / "sent_log.json"


def load_sent():
    if LOG_FILE.exists():
        return set(json.loads(LOG_FILE.read_text()))
    return set()


def save_sent(sent_ids):
    LOG_FILE.write_text(json.dumps(sorted(sent_ids), indent=2))


def due_unsent_poems():
    today = date.today().isoformat()
    sent = load_sent()
    return [
        p for p in POEMS
        if p["reveal_date"] <= today and p["id"] not in sent
    ]


def build_email(poem, recipient, sender):
    msg = EmailMessage()
    msg["Subject"] = f"A poem for you: {poem['title']}"
    msg["From"] = sender
    msg["To"] = recipient

    image_paths = [ROOT / img for img in poem.get("images", []) if (ROOT / img).exists()]

    plain = poem["poem"]
    msg.set_content(plain)

    cids = []
    img_tags = ""
    for i, path in enumerate(image_paths):
        cid = f"image{i}"
        cids.append((cid, path))
        img_tags += f'<img src="cid:{cid}" style="max-width:100%;border-radius:8px;margin:8px 0;"><br>'

    html_body = f"""
    <html><body style="font-family:Georgia,serif;color:#3a332c;max-width:600px;margin:auto;">
      <h2 style="color:#b5654b;font-weight:normal;">{poem['title']}</h2>
      <p style="white-space:pre-wrap;font-size:1.05rem;">{plain}</p>
      {img_tags}
    </body></html>
    """
    msg.add_alternative(html_body, subtype="html")

    # attach images inline to the html alternative
    html_part = msg.get_payload()[-1]
    for cid, path in cids:
        with open(path, "rb") as f:
            html_part.add_related(
                f.read(), maintype="image", subtype=path.suffix.lstrip(".") or "jpeg", cid=f"<{cid}>"
            )

    return msg


def main():
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ.get("SMTP_PORT", 587))
    email_user = os.environ["EMAIL_USER"]
    email_pass = os.environ["EMAIL_PASS"]
    recipient = os.environ["RECIPIENT"]

    poems_to_send = due_unsent_poems()
    if not poems_to_send:
        print("Nothing new to send.")
        return

    sent = load_sent()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_user, email_pass)
        for poem in poems_to_send:
            msg = build_email(poem, recipient, email_user)
            server.send_message(msg)
            sent.add(poem["id"])
            print(f"Sent: {poem['id']} - {poem['title']}")

    save_sent(sent)


if __name__ == "__main__":
    main()
