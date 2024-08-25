class Database:
    from Person import Person

    def __init__(self):
        # establish connection to server
        self.client = None

    def add(self, person: Person):
        # method to add a person int our database
        return None

    def remove(self, person: Person):
        # method to remove person from database
        return None

    def get(self, person: Person = None):
        # get info on a specific person (can have majority None fields), otherwise on all
        return None
