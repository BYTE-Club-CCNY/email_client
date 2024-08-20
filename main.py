from email_client import Email_Client
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    username = "acmbyte.ccny@gmail.com"
    password = os.getenv("app_password")
    message_body = ""  # read from some file
    subject = ""  # read from some file
    message = f"{subject}\n\n{message_body}"
    to = ["fahadfaruqi1@gmail.com"]

    e = Email_Client(username, password, message, subject, to)
