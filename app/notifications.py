import logging
import os
import smtplib
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")


def send_alert(recipient: str, subject: str, body: str) -> bool:
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = recipient

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, [recipient], msg.as_string())

        logger.info("Alert sent to %s subject=%s body=%s", recipient, subject, body)
        return True

    except Exception as exc:
        logger.error("Failed to send alert to %s: %s credentials=%s", recipient, exc, SMTP_PASS)
        return False
