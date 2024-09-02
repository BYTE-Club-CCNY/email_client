""" main entry for application """

from Email import Email
from dotenv import load_dotenv
import os
# from argparse import argparse

# https://docs.python.org/3/library/argparse.html
if __name__ == "__main__":
    from Database import Database
    
    # parser = argparse.ArgumentParser(
    #                 prog='ProgramName',
    #                 description='What the program does',
    #                 epilog='Text at the bottom of help')


    # parser.add_argument('filename')           # positional argument
    # parser.add_argument('-c', '--count')      # option that takes a value
    # parser.add_argument('-v', '--verbose',
    #                     action='store_true')  # on/off flag

    # args = parser.parse_args()
    # print(args.filename, args.count, args.verbose)

    load_dotenv()
    with open('body.html', 'r') as f:
        html_string = f.read()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    to = ["fahadfaruqi1@gmail.com"]

    e = Email(username, password, html_string, "Test", to)
    e.email()

