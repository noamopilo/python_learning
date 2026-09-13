from dotenv import load_dotenv
import os
import smtplib
import ssl

receiver = input("Who do you want to send a mail to (email adress)?: ")
subject = input("What is the subject of the mail you want to send?: ")
msg = input(f"What is the message you want to send?: ")

sender = "nonobal2812@gmail.com"

load_dotenv()  # or load_dotenv(path_to_env)

def send_email(sender, receiver, subject, msg):
    try:
        password = os.environ["password"]
    except KeyError as e:
        print(f"Error: environment variable {e} not found (check your .env file).")
        return

    body_msg = f"""From: {sender}
Subject: {subject}

{msg}
"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, body_msg)
        print("Mail sent!")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

send_email(sender, receiver, subject, msg)
