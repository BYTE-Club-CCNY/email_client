""" implement testing framework for database """


class Test:
    def __init__(self):
        from Database import Database

        self.database = Database()
