""" implement testing framework for database """


class Test:
    def __init__(self):
        from Database import Database

        self.passed_counter = 0
        self.database = Database()

    def load_environment(self):
        try:
            import os
            from dotenv import load_dotenv

            load_dotenv()

            _ = os.getenv("POSTGRESQL_DB")
            _ = os.getenv("POSTGRESQL_DB_USER")
            _ = os.getenv("POSTGRESQL_DB_PASSWORD")
            _ = os.getenv("POSTGRESQL_DB_HOST")
            _ = os.getenv("POSTGRESQL_DB_PORT")

            self.passed_counter += 1
            return True

        except Exception as e:
            print("Failed load environment test")
            print(e)
            return False


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
            _ = self.database.add(t)
            self.passed_counter += 1
            return True
        except Exception as e:
            print("Add Test Unit Test failed\n", e)
            return False

    def get_test(self):
        try:
            _ = self.database.get()
            self.passed_counter += 1
            return True
        except Exception as e:
            print("Get All Values test failed")
            print(e)
            return False


if __name__ == "__main__":
    ut = UnitTest()
    assert ut.load_environment() is True
    assert ut.get_test() is True
    assert ut.add_test() is True
