import os
import smtplib, ssl
from dotenv import load_dotenv

load_dotenv()
google_password = os.getenv("GOOGLE_PASSWORD")


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    username = "cpt2948@gmail.com"
    password = google_password
    receiver_email = "cpt2948@gmail.com"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(username, google_password)
        server.sendmail(username, receiver_email, message)