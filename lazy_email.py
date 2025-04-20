from smtplib import SMTP_SSL
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import pandas as pd


#pandas stuff
#df= pd.read_csv("your.csv")

#emails= df[df['Final verdict']=='Accepted']['Email Address'].tolist()
#emails=df['Final verdict'].unique() #debug


'''
or if you have a list of emails you wanna just send to, 
comment all the dataframe stuff above and uncomment this below
then add any emails you want to send to in the list below
'''
emails = []



emails.append("acmbyte.ccny@gmail.com") #include self
#print(emails) #debug

#setup envs
load_dotenv()
username = os.getenv("EM_USERNAME")
password = os.getenv("EM_PASSWORD")#ask fahad or jawad for .env

#smtp config
mailserver = "smtp.gmail.com"
serverPort = 465


with open("body.html", "r") as file: #make sure body.html in root. double check cdn for byte logo
    email_body = file.read()

#email structure
subject = "BYTE x Google AI Labs Update"
recipients = emails

with SMTP_SSL(mailserver, serverPort) as server:
    try:
        server.ehlo()
        server.login(username, password)

        for recipient in recipients:
            mime_message = MIMEMultipart("alternative")
            mime_message["From"] = username
            mime_message["To"] = recipient
            mime_message["Subject"] = subject
            mime_message.attach(MIMEText(email_body, "plain"))
            mime_message.attach(MIMEText(email_body, "html"))

            server.sendmail(username, recipient, mime_message.as_string())

        server.quit()
        print("Emails sent successfully")
    except smtplib.SMTPRecipientsRefused as e:
        print("All recipient addresses refused, no one got an email", e.recipients)
        exit(1)
    except smtplib.SMTPHeloError as e:
        print("Error connecting to SMTP server", e)
        exit(1)
    except smtplib.SMTPSenderRefused as e:
        print("Server did not accept the sender's address", e)
        exit(1)
