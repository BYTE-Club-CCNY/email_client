""" contains all details on a person that are relevant and in database """


class Person:
    def __init__(
        self,
        uid: str = None,
        first_name: str = "",
        middle_name: str = "",
        last_name: str = "",
        school_email: str = None,
        personal_email: str = None,
        preferred_email: bool = False,
        active: bool = None,
        emplid: str = None,
        discord: str = None,
    ):
        self.uid = None
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.school_email = school_email
        self.personal_email = personal_email
        self.preferred_email = preferred_email
        self.active = active
        self.discord = discord
        self.emplid = emplid

    def add_person(self):
        from Database import Database
        from Validation import Input

        # color?

        print(
            "Input New User Information (* means manditory)\nOptional fields you can leave blank.\n^c to exit"
        )

        try:
            full_name = Input("Full Name*: ", str).val.split(" ")
            self.first_name = full_name[0]

            if len(full_name) > 1:
                self.last_name = full_name[-1]

                middle_name = " ".join(full_name[1:-1])
                self.middle_name = middle_name if middle_name != "" else None

            self.school_email = Input("School Email*: ", str).val
            self.personal_email = Input(
                "Personal Email (assumed to be preferred): ", str, True
            ).val

            if self.personal_email:
                self.preferred_email = True

            self.active = Input("Active BYTE member? (y/n)*: ", bool).val
            self.discord = Input("Discord: ", str, True).val
            self.emplid = Input("Emplid*: ", int).val

        except KeyboardInterrupt:
            exit(1)

        d = Database()
        d.add(self)
        return

