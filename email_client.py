class Email_Client:
    def __init__(
        self,
        username: str,
        password: str,
        message: str,
        subject: str,
        to: list[str],
        cc: list[str] = None,
    ):
        self.mailserver = "smtp.gmail.com"  # server host we will be using
        self.serverPort = 465
        self.username = username
        self.password = password
        self.message = "Subject: {}\n\n{}".format(subject, message)
        self.to = to
        self.cc = cc  # should always include all active cabinet members

    def add_to(self, to: str | list[str]):
        if isinstance(to, str):
            self.to.append(to)
        else:
            self.to.append(*to)

    # will open an smpt server
    def email(self):
        from smtplib import SMTP_SSL
        import smtplib

        with SMTP_SSL(self.mailserver, self.serverPort) as server:
            try:
                server.ehlo()
                server.login(self.username, self.password)
                server.sendmail(self.username, self.to, self.message)
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
            except Exception as e:
                print(f"Unhandled Exception occured!\n {str(e)}")
