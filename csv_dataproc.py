import pandas as pd
import numpy as np
from Person import Person
from Database import Database
db = Database()
df=pd.read_csv('data/B.Y.T.E Club Form (Responses) - Form Responses.csv')
df2=pd.read_csv('data/Team Grouping (Responses) - Form Responses.csv')
df=df.merge(df2,on='What is your name?', how='left')
df.drop_duplicates(subset=['What is your name?']) #removes weird edge cases

#print(df.columns) #ignore, this is just for reference when i was building -jawad
for index,row in df.iterrows():
    name_arr = row['What is your name?'].split(' ')
    middle = ""
    if len(name_arr) > 2:
        middle = ' '.join(name_arr[1:-1])

    #print(row['What is your EMPLID']) #ignore, debugging line
    new_person = Person(
    None,
    name_arr[0],
    middle,
    name_arr[-1],
    row['What is your CityMail?'],
    row['if you prefer we contact your personal email, please put it here'],
    pd.notna(row['if you prefer we contact your personal email, please put it here']), #had to use gpt :(
    False, #active bool. by default is false for all members.
    row['What is your EMPLID'],
    row["What's your discord?"]
    )

    db.add(new_person)
    
