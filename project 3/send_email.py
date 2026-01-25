import smtplib, ssl
import os # hide password

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "cpt2948@gmail.com"
    password = os.getenv("email app")

    receiver = "cpt2948@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        

#send_email("Hello, Here the news topics")
