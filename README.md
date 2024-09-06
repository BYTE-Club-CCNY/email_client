## BYTE Emailer
Hello. This is the BYTE mass email project designed by Jawad Kabir and Fahad Faruqi. The main goal of this app is to push an email to a large amount of club members without the need of using external software like mailchimp. While those software are free and easy to use, as BYTE SWEs we have the tools and the capability of creating software for any of our needs, so why not make our own application? 

This application interfaces with the database server developed and maintained by @lordfarquaadthecreator in our AWS EC2 server. All of our applicants and alumni are included in this database (schema in `/database`). 
The CLI (`main.py`) currently has the ability to get users by first name, add people to our blacklist (by uid) and send emails to everyone, our cabinet or only active BYTE members. 

## Getting Started
To install all of the dependencies, you'll need to first make a virtual environment like so :
```bash
python3 -m venv env
```
Next, you'll want to activate the venv like so:
```bash
# Unix (better)
source env/bin/activate
# Windows
.venv/Scripts/activate
```
Next, pip install your dependencies
```bash
pip3 install -r req.txt
```

Create a file called `body.html` where the body of the email will be developed. *This file is not tracked.*
And now you should be good to go!

If you're confused, use the `-h` flag for help. 
