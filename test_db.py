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


#uid = db.add(new_person)
#db.add_cabinet(uid[0])

db.remove(['71343118-4947-4411-b440-453448beb10b'])
cabinet_members = db.get_cabinet()
print("Cabinet members:", cabinet_members)
print(db.get_all())


