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

    parser.add_argument(
        "-a", "--active", type=str, help="email all active members only"
    )
    parser.add_argument(
        "-c", "--cabinet", type=str, help="email all cabinet members only"
    )
    parser.add_argument(
        "-all", "--all", type=str, help="email everyone in our database minus blacklist"
    )
    parser.add_argument(
        "-s",
        "--specific",
        type=str,
        nargs="+",
        help="email specifically these people, last argument is the subject",
    )
    parser.add_argument("-g", "--get-person", type=str, help="get person by first name")
    parser.add_argument("-b", "--add-blacklist", help="add person to blacklist by uid")
    parser.add_argument(
        "-add",
        "--add-person",
        action="store_true",
        help="start CLI to add person into database",
    )
    parser.add_argument(
        "-r", "--remove-person", type=str, nargs="+", help="remove people from database"
    )
    parser.add_argument("-ac", "--add-cabinet", type=str, help="add uid to cabinet")
    parser.add_argument(
        "-rc", "--remove-cabinet", type=str, help="remove uid from cabinet"
    )

    args = parser.parse_args()

    if args.specific:
        e = Email(html_string, args.specific[0:-1], args.specific[-1])
        e.email()

    if args.add_person:
        from Person import Person

        ad = Person()
        ad.add_person()
        exit(0)

    if args.remove_person:
        d = Database()

        d.remove(args.remove_person)
        exit(0)

    if args.add_cabinet:
        d.add_cabinet(args.add_cabinet)
        exit(0)

    if args.remove_cabinet:
        d.del_cabinet(args.remove_cabinet)
        exit(0)

    if args.add_blacklist is not None:
        d.add_blacklist(args.add_blacklist)
        exit(0)

    if args.get_person is not None:
        res = d.get_person_by_name(args.get_person)
        print(res)
        exit(0)

    if args.cabinet:
        e = Email(html_string, args.cabinet, d.get_cabinet())
        e.email()

    if args.active:
        e = Email(html_string, args.active, d.get_active())
        # e.email()

    if args.all:
        e = Email(html_string, args.all, d.get_all())
        # e.email()
