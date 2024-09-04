from Database import Database
from Person import Person

# Create a Person object

new_person = Person(
    None,
    "Jawad",
    "S.",
    "Kabir",
    'abcd@gmail.com',
    'abcd@citymail.cuny.edu',
    True,
    True,
    '#TotallySaber',
    "12345678"
)

db = Database()


#=uid = db.add(new_person)
#db.add_cabinet(uid[0])
db.del_cabinet(['98f04bf9-972a-46c1-9234-2129eb99492e'])
cabinet_members = db.get_cabinet()
print("Cabinet members:", cabinet_members)



