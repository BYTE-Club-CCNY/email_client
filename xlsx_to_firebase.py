from socket import *
from smtplib import SMTP_SSL
from dotenv import load_dotenv
import os
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd #dependencies, self-explanatory
import openpyxl
load_dotenv() #load env variables

#data science stuff go brrrr
#btt knowledge go crazy
df=pd.read_excel('B.Y.T.E Club Form (Responses).xlsx')
names_emails_tuples = list(zip(df['What is your name?'], df['Email Address']))

#firebase login, requires firebase.json to exist
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('dbUrl') #this is my db url
})

#function to add to the db. we will be calling this a few times to push from the xlsx/csv files.
def push_db(name, email):
    # we use email as a unique identifier by replacing '.' with ',' since '.' is flagged by firebase
    user_id = email.replace('.', ',')
    ref = db.reference(f'users/{user_id}')
    user_data = {
        'name': name,
        'email': email
    }
    ref.set(user_data)
def get_emails():
    ref = db.reference('users')
    users = ref.get()
    
    if users is not None:
        emails = [user_data['email'] for user_data in users.values() if 'email' in user_data]
        return emails
    else:
        return []
#main (im lazy)
for name,email in names_emails_tuples:
    push_db(name, email)
print(get_emails())
