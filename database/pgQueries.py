class pgQueries:
    def __init__(self):
        self.select_blacklist = """ SELECT                                     
                                        CASE 
                                            WHEN preferred_email = true THEN personal_email 
                                            ELSE cuny_email 
                                        END AS email
                                    FROM people
                                    WHERE uid NOT IN (SELECT uid FROM blacklist)
                                """
        self.select_cabinet = """ SELECT 
                                    CASE 
                                        WHEN preferred_email = true THEN personal_email 
                                        ELSE cuny_email 
                                    END AS email
                                FROM people
                                WHERE uid IN (SELECT uid FROM cabinet);
                                """
        self.select_all_no_blacklist = """ SELECT 
                                            CASE 
                                                WHEN preferred_email = true THEN personal_email 
                                                ELSE cuny_email 
                                            END AS email
                                            FROM people 
                                           WHERE uid NOT IN (SELECT uid from blacklist) """
        self.select_all = """ SELECT                                     
                                CASE 
                                    WHEN preferred_email = true THEN personal_email 
                                    ELSE cuny_email 
                                END AS email
                             FROM people """

        self.select_people = (
            """ SELECT * from PEOPLE WHERE first_name in (%s) """
        )
        self.select_active = """ SELECT                                     
                                    CASE 
                                        WHEN preferred_email = true THEN personal_email 
                                        ELSE cuny_email 
                                    END AS email
                                FROM people where active = 1 """

        self.add_cabinet = """ INSERT INTO cabinet (uid) VALUES (%s) """
        self.remove_cabinet = """DELETE FROM cabinet WHERE uid=%s"""
        self.add_blacklist = """ INSERT INTO blacklist (uid) VALUES (%s) """
        self.delete_person = """ DELETE FROM people WHERE uid = (%s) """
        self.add_person = """ INSERT INTO people (first_name, middle_name, last_name, 
                                personal_email, cuny_email, preferred_email,active, discord, emplid)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING uid"""
        self.mark_inactive = """ UPDATE people SET active = false WHERE uid = (%s) """
        self.mark_active = """ UPDATE people SET active = true WHERE uid = (%s) """
