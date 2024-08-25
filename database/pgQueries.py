class pgQueries:
    def __init__(self):
        self.select_blacklist = """SELECT *
                                FROM people
                                WHERE uid NOT IN (SELECT uid FROM blacklist);
                                """
        self.select_cabinet = """SELECT *
                                FROM people
                                WHERE uid IN (SELECT uid FROM cabinet);
                                """
        self.select_all_no_blacklist = """ SELECT * FROM people 
                                           WHERE uid NOT IN (SELECT uid from blacklist) """
        self.select_all = """ SELECT * FROM people """
        self.add_cabinet = """ INSERT INTO cabinet (uid) VALUES (%s) """
        self.add_blacklist = """ INSERT INTO blacklist (uid) VALUES (%s) """
        self.delete_person = """ DELETE FROM people WHERE uid = (%s) """
        self.add_person = """ INSERT INTO people (first_name, middle_name, last_name, 
                                personal_email, cuny_email, preferred_email, discord, emplid)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
