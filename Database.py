""" establishes connection to database and prefroms actions based on person objects """


class Database:
    from Person import Person

    def __init__(self):
        from database.pgQueries import pgQueries

        self.queries = pgQueries()

    # execute in a try catch
    def execute_query(self, query: str, values: list, return_output: bool = False):
        import psycopg
        from dotenv import load_dotenv
        import os

        load_dotenv()

        res = None

        db_name = os.getenv("POSTGRESQL_DB")
        db_user = os.getenv("POSTGRESQL_DB_USER")
        db_password = os.getenv("POSTGRESQL_DB_PASSWORD")
        db_host = os.getenv("POSTGRESQL_DB_HOST")
        db_port = os.getenv("POSTGRESQL_DB_PORT")

        with psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)

                if return_output:
                    res = cur.fetchall()
                else:
                    res = True
                conn.commit()
        return res

    def add(self, person: Person):
        query = self.queries.add_person
        values = [
            person.first_name,
            person.middle_name,
            person.last_name,
            person.personal_email,
            person.school_email,
            person.preferred_email,
            person.discord,
            person.emplid,
        ]
        return self.execute_query(query, values, True)

    def remove(self, people: list[str] or str):
        query = self.queries.delete_person

        if not isinstance(people, list):
            people = [people]
        try:
            self.execute_query(query, people)
            return True
        except Exception as e:
            return e

    def get(self, person: Person = None, select_blacklist: bool = False):
        if not person:
            if not select_blacklist:
                query = self.queries.select_all_no_blacklist
            else:
                query = self.queries.select_all
            values = []

            try:
                res = self.execute_query(query, values, True)
                return res
            except Exception as e:
                print("Exception Occured", e)
                return None
        else:
            query = self.queries.select_all
            # if UID present, that trumps all
            if person.uid:
                try:
                    query += " WHERE UID = (%s)"
                    values = person.uid
                    res = self.execute_query(query, values, True)
                    return res
                except Exception as e:
                    print("exception occured", e)
                    return None

            # build query based on what values are avaiable
            # iterate over all public fields in the class and construct a LIKE % % query for them
            # person object must not contain methods
            fields = [a for a in dir(person) if not a.startswith("__")]
            query += " WHERE"
            for field in fields:
                query += f" {field} LIKE %{getattr(person, field)}%,\n"

            try:
                return self.execute_query(query, [], True)
            except Exception as e:
                print("Exception Occured", e)
                return None

    def add_cabinet(self, person: Person):
        query = self.queries.add_cabinet
        values = person.uid

        try:
            res = self.execute_query(query, values)
            return res
        except Exception as e:
            print("Exception Occured", e)
            return None

    def get_cabinet(self):
        query = self.queries.select_cabinet
        try:
            response = self.execute_query(query, (), True)
            arr = []

            for res in response:
                arr.append(res[0])
            return arr
        except Exception as e:
            print("Exception occured:", e)
            return None

    def get_active(self):
        query = self.queries.select_active
        try:
            response = self.execute_query(query, (), True)
            arr = []

            for res in response:
                arr.append(res[0])
            return arr
        except Exception as e:
            print("Exception occured:", e)
            return None

    def get_all(self):
        query = self.queries.select_all_no_blacklist
        try:
            response = self.execute_query(query, (), True)
            arr = []

            for res in response:
                arr.append(res[0])
            return arr
        except Exception as e:
            print("Exception occured:", e)
            return None

    def select_blacklist(self):
        query = self.queries.select_blacklist
        try:
            res = self.execute_query(query, (), True)
            return res
        except Exception as e:
            print("Exception occured:", e)
            return None

    def add_blacklist(self, person: Person):
        query = self.queries.add_blacklist
        values = person.uid

        try:
            res = self.execute_query(query, values)
            return res
        except Exception as e:
            print("Exception occured:", e)
            return None

        return None
