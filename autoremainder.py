import unittest
import imaplib
import smtplib
import email
from email.mime.text import MIMEText

# e-maila config
EMAIL_ADDRESS = "my_email@gmail.com"
EMAIL_PASSWORD = "my_password"
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def check_unread_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")
    
    result, data = mail.search(None, "UNSEEN")
    unread_msg_nums = data[0].split()
    
    emails = []
    for num in unread_msg_nums:
        result, msg_data = mail.fetch(num, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                emails.append(msg["From"])  # getting email sender
    
    mail.logout()
    return emails

def send_auto_reply(recipient):
    msg = MIMEText("Dziękujemy za wiadomość! Odpowiemy wkrótce.")
    msg["Subject"] = "Automatyczna odpowiedź"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
    server.quit()

def automate_email_response():
    unread_senders = check_unread_emails()
    for sender in unread_senders:
        send_auto_reply(sender)
    print("Automatyczne odpowiedzi zostały wysłane.")