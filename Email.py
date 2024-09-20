class Email:
    def __init__(
        self,
        message: str,
        subject: str,
        to: list[str],
        cc: list[str] = None,
    ):
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        import os
        from dotenv import load_dotenv

        load_dotenv()

        username = os.getenv("EM_USERNAME")    #note for jawad in the future, this should be edited to EM_USERNAME, due to a path variable named username existing.
        password = os.getenv("EM_PASSWORD")
        if not username or not password:
            raise Exception("missing environment variables USERNAME or PASSWORD")

        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = subject
        self.message["From"] = username
        self.message["To"] = ", ".join(
            to
        )  # should send to BYTE account and in isolation!
        self.message["Cc"] = ", ".join(cc) if cc else ""
        self.message.attach(MIMEText(message, "plain"))
        self.message.attach(MIMEText(message, "html"))

        self.mailserver = "smtp.gmail.com"
        self.serverPort = 465
        self.username = username
        self.password = password
        self.to = to
        self.cc = cc

    # will open an smpt server
    def email(self):
        from smtplib import SMTP_SSL
        import smtplib

        with SMTP_SSL(self.mailserver, self.serverPort) as server:
            try:
                server.ehlo()
                server.login(self.username, self.password)

                for to in self.to:
                    server.sendmail(self.username, to, self.message.as_string())

                server.quit()
                print("Email Sent")
            except smtplib.SMTPRecipientsRefused as e:
                print(
                    "All recipient addresses refused, no one got an email", e.recipients
                )
                exit(1)
            except smtplib.SMTPHeloError as e:
                print("Error connecting to SMPT server", e)
                exit(1)
            except smtplib.SMTPSenderRefused as e:
                print("Server did not accept one of the 'to' addresses", e)
                exit(1)
