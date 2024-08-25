""" establishes connection to database and prefroms actions based on person objects """


class Database:
    from Person import Person

    # execute in a try catch
    def execute_query(self, query: str, values: list):
        import psycopg
        from dotenv import load_dotenv
        import os

        load_dotenv()

        res = []

        db_name = os.getenv("POSTGRESQL_DB")
        db_user = os.getenv("POSTGRESQL_DB_USER")

        with psycopg.connect(f"dbname={db_name} user={db_user}") as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                cur.fetchall()

                for record in cur:
                    res.append(cur)

                conn.commit()

        return res

    def add(self, person: Person):
        # method to add a person int our database
        return None

    def remove(self, person: Person):
        # method to remove person from database
        return None

    def get(self, person: Person = None, blacklist: bool = False):
        # get info on a specific person (can have majority None fields), otherwise on all
        return None

    def add_cabinet(self, person: Person):
        # adds into cabinet table
        return None

    def select_cabinet(self):
        return None

    def select_blacklist(self):
        return None

    def add_blacklist(self):
        return None
