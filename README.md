## BYTE Emailer
Hello. This is the BYTE mass email project designed by Jawad Kabir and Fahad Faruqi. The main goal of this app is to push an email to a large amount of club members without the need of using external software like mailchimp. While those software are free and easy to use, as computer science majors we have the tools and the capability of creating software for any of our needs, so why not make our own application that pushes our messages. This isn't intended to be the most robust application ever, but it is meant to be easy to use. We want to be able to reach all of our members without having a "2 emails per month" or any other limitation that another mail service has. 
## Getting Started
To install all of the dependencies, you'll need to first make a virtual environment like so :
```bash
py -m venv .venv
```
Next, you'll want to activate the venv like so:
```bash
.venv/Scripts/activate
```
Next, pip install your dependencies
```bash
pip install -r req.txt
```
And now you should be good to go!
## Functionalities
So with this project I used a PostgreSQL database to hold the emails of well over 200+ members. This will be scraped from our csv files that we place as an input (for safety these have been omitted). We would then pipe the emails into the email client through pandas manipulation, and then using smtp connection to the google server, we will push all the emails to the recipients' accounts. We have implemented command line arguments to enable ease of access. 
