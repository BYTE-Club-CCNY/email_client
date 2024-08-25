""" establishes connection to database and prefroms actions based on person objects """


class Database:
    from Person import Person

    def __init__(self):
        from database.pgQueries import pgQueries

        self.queries = pgQueries()

    # execute in a try catch
    def execute_query(self, query: str, values: list):
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
                res = cur.fetchall()

                conn.commit()

        return res

    def add(self, person: Person):
        # method to add a person int our database
        return None

    def remove(self, person: list[Person]):
        query = self.queries.delete_person

        values = []
        for p in person:
            values.append(p.uid)

        try:
            self.execute_query(query, values)
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
                res = self.execute_query(query, values)
                return res
            except Exception as e:
                print("Exception Occured", e)
                return None
        else:
            # build query based on what values are avaiable
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

    def select_cabinet(self):
        query = self.queries.select_cabinet
        try:
            res = self.execute_query(query, ())
            return res
        except Exception as e:
            print("Exception occured:", e)
            return None

    def select_blacklist(self):
        query = self.queries.select_blacklist
        try:
            res = self.execute_query(query, ())
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
