""" strictly for testing only - main entry should be via post request"""

from Email import Email
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    from Database import Database

    d = Database()
    d.select_cabinet()
    # load_dotenv()
    # username = os.getenv("username")
    # password = os.getenv("password")

    # if not username or not password:
    #     print("username or password not found")
    #     print(f"Username: {username} \nPassword: {password}")
    #     exit(1)

    # message_body = "hiiiiii"  # read from some file
    # subject = "hi"  # read from some file
    # message = f"{subject}\n\n{message_body}"
    # to = ["fahadfaruqi1@gmail.com"]

    # e = Email_Client(username, password, message, subject, to)
    # e.email()
