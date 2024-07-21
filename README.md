## BYTE Emailer
Hello. This is the BYTE mass email project designed by Jawad Kabir. The main goal of this app is to push an email to a large amount of club members without the need of using external software like mailchimp. While those software are free and easy to use, as computer science majors we have the tools and the capability of creating software for any of our needs, so why not make our own application that pushes our messages. This isn't intended to be the most robust application ever, but it is meant to be easy to use. We want to be able to reach all of our members without having a "2 emails per month" or any other limitation that another mail service has. 
## Getting Started
Make sure you install the dependencies using the following command
```pip install -r requirements.txt```

## Functionalities
So with this project I used a Firebase database to hold the emails of well over 200+ members. This will be scraped from our xlsx file that we place as an input. We would then pipe the emails into the email client through querying, and then using smtp connection to the google server, we will push all the emails to the recipients' accounts. Other than that, I intend to create a FastAPI backend just for the sake of having one. Not entirely sure if I will implement a front end, prob will. 

## To Do List
- [ ] Implement routes
- [ ] Implement input system for csv file
- [ ] Implement scheduling for emails