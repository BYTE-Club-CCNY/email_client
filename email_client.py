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
        self.subject = subject  # jawad had this as 'subject: ' + subject string -- why?
        self.message = f"{subject}\n\n{message}"
        self.to = to
        self.cc = cc

    # will open an smpt server
    def email(self):
        from smtplib import SMTP_SSL

        with SMTP_SSL(self.mailserver, self.serverPort) as server:
            try:
                server.ehlo()
                server.login(self.username, self.password)
                server.sendmail(self.username, self.recipient, self.message)
                server.quit()
                print("Email Sent")
            except Exception as e:
                print(f"Unhandled Exception occured!\n {str(e)}")
