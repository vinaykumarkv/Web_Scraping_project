import smtplib, ssl

import os
from dotenv import load_dotenv
load_dotenv()
sender = os.getenv("sender")
receiver = os.getenv("receiver")
password = os.getenv("password")
context = ssl.create_default_context()
host = "smtp.gmail.com"
port = 465
def emailer(email_body, sender= sender, to= receiver, subject="Test Email"):
    # Create the email
    sender = sender
    to = to
    subject = subject
    body = email_body
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, to, body.encode('utf-8'))
    print("email sent!")
