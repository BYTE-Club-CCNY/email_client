""" implement testing framework for database """


class Test:
    def __init__(self):
        from Database import Database

        self.failed = False
        self.database = Database()
        self.uid_to_delete = ""

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
            print(user, password, db, db_host, db_pass, db_port, db_user)
            raise Exception("Missing Certain Environment Variables")
        return True


class UnitTest(Test):
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

    def get_test(self):
        try:
            _ = self.database.get()
            return True
        except Exception as e:
            self.failed = True
            print("Get All Values test failed")
            print(e)
            return False


if __name__ == "__main__":
    ut = UnitTest()

    ut.load_environment()
    ut.add_test()
    ut.get_test()
    ut.delete_test()

    if ut.failed:
        print("Tests Failed")
        exit(1)
    print("Tests Passed!")
    exit(0)
