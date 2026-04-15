import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email(sender, password, receiver, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)

        server.send_message(msg)
        server.quit()

        return True, "Sent"

    except Exception as e:
        return False, str(e)


def send_with_retry(sender, password, receiver, subject, body, retries=3):
    for attempt in range(retries):
        success, message = send_email(sender, password, receiver, subject, body)
        if success:
            return True, message
        print(f"Retrying... ({attempt+1})")
        time.sleep(2)

    return False, message