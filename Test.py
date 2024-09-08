""" implement testing framework for database """


class Test:
    def __init__(self):
        self.failed = False

    def load_environment(self):
        import os
        from dotenv import load_dotenv

        load_dotenv()

        user = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        db = os.getenv("POSTGRESQL_DB")
        db_user = os.getenv("POSTGRESQL_DB_USER")
        db_pass = os.getenv("POSTGRESQL_DB_PASSWORD")
        db_host = os.getenv("POSTGRESQL_DB_HOST")
        db_port = os.getenv("POSTGRESQL_DB_PORT")

        if (
            not db
            or not db_user
            or not db_pass
            or not db_host
            or not db_port
            or not password
            or not user
        ):
            raise Exception("Missing Certain Environment Variables")
        return True


class DatabaseTest(Test):
    def __init__(self):
        from Database import Database

        self.database = Database()
        self.uid_to_delete = ""

    def add_test(self):
        from Person import Person

        t = Person(
            None,
            "Saul",
            "Good",
            "Man",
            "www.google.com",
            "www.google.com",
            True,
            True,
            "12345",
            "user",
        )

        try:
            res = self.database.add(t)[0]
            self.uid_to_delete = str(res[0])
            return True
        except Exception as e:
            self.failed = True
            print("Add Test Unit Test failed\n", e)
            return False

    def delete_test(self):
        try:
            self.database.remove(self.uid_to_delete)
            return True
        except Exception:
            self.failed = True
            raise Exception("Deleting User Test Failed")

    def get_test(self):  # bad test
        try:
            res = self.database.get()
            assert len(res) > 0
            return True
        except Exception as e:
            self.failed = True
            print("Get All Values test failed")
            print(e)
            return False


class SQLTest(Test):
    def __init__(self):
        from database.pgQueries import pgQueries

        self.queries = pgQueries()

    def check_queries_exist(self):
        try:
            assert len(self.queries.select_blacklist) > 0 and isinstance(
                self.queries.select_blacklist, str
            )
            assert len(self.queries.select_cabinet) > 0 and isinstance(
                self.queries.select_cabinet, str
            )
            assert len(self.queries.select_all_no_blacklist) > 0 and isinstance(
                self.queries.select_all_no_blacklist, str
            )
            assert len(self.queries.select_all) > 0 and isinstance(
                self.queries.select_all, str
            )

            assert len(self.queries.select_people) > 0 and isinstance(
                self.queries.select_people, str
            )
            assert len(self.queries.select_active) > 0 and isinstance(
                self.queries.select_active, str
            )

            assert len(self.queries.remove_cabinet) > 0 and isinstance(
                self.queries.remove_cabinet, str
            )
            assert len(self.queries.delete_person) > 0 and isinstance(
                self.queries.delete_person, str
            )

            assert len(self.queries.mark_active) > 0 and isinstance(
                self.queries.mark_active, str
            )
            assert len(self.queries.mark_inactive) > 0 and isinstance(
                self.queries.mark_inactive, str
            )
            assert len(self.queries.mark_all_inactive) > 0 and isinstance(
                self.queries.mark_all_inactive, str
            )

            assert len(self.queries.add_blacklist) > 0 and isinstance(
                self.queries.add_blacklist, str
            )
            assert len(self.queries.add_cabinet) > 0 and isinstance(
                self.queries.add_cabinet, str
            )
            assert len(self.queries.add_person) > 0 and isinstance(
                self.queries.add_person, str
            )

        except AttributeError as e:
            print("pgQueries class is missing the following query: ", e.name)
            self.failed *= 1


if __name__ == "__main__":
    pgTest = SQLTest()
    dbTest = DatabaseTest()

    pgTest.check_queries_exist()

    dbTest.load_environment()
    dbTest.add_test()
    dbTest.get_test()
    dbTest.delete_test()

    if dbTest.failed or pgTest.failed:
        print("Tests Failed")
        exit(1)
    print("Tests Passed!")
    exit(0)
