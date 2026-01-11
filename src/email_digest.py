# src/email_digest.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Dict


def send_email_digest(
    articles: List[Dict],
    dashboard_url: str,
    sender_email: str,
    receiver_email: str,
    app_password: str,
):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📈 Indian Market Intraday News Digest"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    html = """
    <html>
    <body>
        <h2>Top 10 Latest Market News</h2>
        <ol>
    """

    for art in articles[:10]:
        html += f"""
        <li>
            <b>{art['title']}</b><br/>
            <small>{art['published_at']}</small><br/>
            {art.get('summary', art.get('content', ''))}<br/>
            <a href="{art['url']}">Read full article</a>
        </li><br/>
        """

    html += f"""
        </ol>
        <hr/>
        <p>
            🔗 <a href="{dashboard_url}">
            View full intraday dashboard
            </a>
        </p>
    </body>
    </html>
    """

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
