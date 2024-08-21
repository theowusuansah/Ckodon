import csv
from email.message import EmailMessage
import smtplib


def get_credentials(filepath):
    with open(filepath, "r") as f:
        email_address = f.readline().strip()
        email_pass = f.readline().strip()
    return email_address, email_pass


def login(email_address, email_pass, s):
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email_address, email_pass)
    print("login")


def send_mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    email_address, email_pass = get_credentials("./credentials.txt")
    login(email_address, email_pass, s)

    # Message to be sent
    subject = ""
    body = """ """

    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            recipient = row[0]
            message = EmailMessage()
            message.set_content(body)
            message['Subject'] = subject
            message['From'] = email_address
            message['To'] = recipient

            s.send_message(message)
            print("Sent To " + recipient)

    # Terminating the session
    s.quit()
    print("Sent")


if __name__ == "__main__":
    send_mail()
