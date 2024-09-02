""" main entry for application """

from Email import Email
from dotenv import load_dotenv
import os
import argparse
from Database import Database

# https://docs.python.org/3/library/argparse.html
if __name__ == "__main__":
    PATH = os.path.join(os.getcwd(), "body.html")
    if not os.path.exists(PATH):
        raise Exception("body.html missing")

    with open(PATH, "r") as f:
        html_string = f.read()

    to = []
    d = Database()

    parser = argparse.ArgumentParser(
        prog="BYTE Email Client",
        description="Emails clients using database of current and previous BYTE applicants. Takes body from body.html. Defaults to emailing all in database regardless of active member",
    )

    parser.add_argument("subject")
    parser.add_argument("-a", "--active", action="store_true")
    parser.add_argument("-c", "--cabinet", action="store_true")

    args = parser.parse_args()

    if not isinstance(args.subject, str):
        raise Exception("Subject must be a string")

    if args.cabinet:
        to.extend(d.get_cabinet())

    if args.active:
        to.extend(d.get_active())

    if not args.active and not args.cabinet:
        to.extend(d.get_all())

    to.append("fahadfaruqi1@gmail.com")  # testing only
    e = Email(html_string, args.subject, to)
    e.email()
