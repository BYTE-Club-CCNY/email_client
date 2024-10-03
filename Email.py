class Email:
    def __init__(
        self,
        message: str,
        subject: str,
        to: list[str],
        cc: list[str] = None,
    ):
        import os
        from dotenv import load_dotenv

        load_dotenv()

        username = os.getenv("EM_USERNAME")
        password = os.getenv("EM_PASSWORD")
        if not username or not password:
            raise Exception("missing environment variables EM_USERNAME or EM_PASSWORD")

        self.mailserver = "smtp.gmail.com"
        self.serverPort = 465
        self.username = username
        self.password = password
        self.to = to
        self.cc = cc
        self.subject = subject
        self.message = message

    def email(self):
        from smtplib import SMTP_SSL
        import smtplib

        with SMTP_SSL(self.mailserver, self.serverPort) as server:
            try:
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText

                server.ehlo()
                server.login(self.username, self.password)

                for recipient in self.to:

                    mime_message = MIMEMultipart("alternative")
                    mime_message["From"] = self.username
                    mime_message["To"] = recipient
                    mime_message["Cc"] = ", ".join(self.cc) if self.cc else ""
                    mime_message["Subject"] = self.subject
                    mime_message.attach(MIMEText(self.message, "plain"))
                    mime_message.attach(MIMEText(self.message, "html"))

                    server.sendmail(self.username, recipient, mime_message.as_string())

                server.quit()
                print("Emails sent successfully")
            except smtplib.SMTPRecipientsRefused as e:
                print(
                    "All recipient addresses refused, no one got an email", e.recipients
                )
                exit(1)
            except smtplib.SMTPHeloError as e:
                print("Error connecting to SMTP server", e)
                exit(1)
            except smtplib.SMTPSenderRefused as e:
                print("Server did not accept the sender's address", e)
                exit(1)
