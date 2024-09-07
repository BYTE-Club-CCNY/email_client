""" main entry for application """

from Email import Email
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
        description="Emails clients using database of current and previous BYTE applicants. Takes body from body.html. Defaults to emailing all in database regardless of active member. Blacklisted folks are ignored by default, unless specified otherwise",
    )

    # parser.add_argument("subject")
    parser.add_argument(
        "-a", "--active", action="store_true", help="email all active members only"
    )
    parser.add_argument(
        "-c", "--cabinet", action="store_true", help="email all cabinet members only"
    )
    parser.add_argument(
        "-t", "--testing", action="store_true", help="testing, won't send an email"
    )
    parser.add_argument("-g", "--get-person", type=str, help="get person by first name")
    parser.add_argument("-b", "--add-blacklist", help="add person to blacklist by uid")
    parser.add_argument(
        "-add",
        "--add-person",
        action="store_true",
        help="start program to add person into database",
    )

    args = parser.parse_args()

    if args.add_person:
        from Person import Person

        ad = Person()
        ad.add_person()
        exit(0)

    if args.add_blacklist is not None:
        d.add_blacklist(args.add_blacklist)
        exit(0)

    if args.get_person is not None:
        res = d.get_person_by_name(args.get_person)
        print(res)
        exit(0)

    if not isinstance(args.subject, str):
        raise Exception("Subject must be a string")

    if args.cabinet:
        to.extend(d.get_cabinet())

    if args.active:
        to.extend(d.get_active())

    if not args.active and not args.cabinet:
        to.extend(d.get_all())

    if not args.testing:
        e = Email(html_string, args.subject, to)
        # e.email()
