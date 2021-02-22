import smtplib
from os import environ

# A class that is used to send an email


class email:

    def __init__(self):
        self.sender_email = environ['SENDER_EMAIL']
        self.rec_email = environ['RECEIVER_EMAIL']
        self.password = environ['SENDER_EMAIL_PASSWORD']

    def send_email(self, subject, message):
        text = "\r\n".join([
            f"From: {self.sender_email}",
            f"To: {self.rec_email}",
            f"Subject: {subject}",
            "",
            f"{message}"
        ])

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(self.sender_email, self.password)
        print("Login success")
        server.sendmail(self.sender_email, self.rec_email, text)
        print("Email has been sent to ", self.rec_email)
