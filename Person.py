""" contains all details on a person that are relevant and in database """


class Person:
    def __init__(
        self,
        uid: str = None,
        first_name: str = None,
        middle_name: str = None,
        last_name: str = None,
        school_email: str = None,
        personal_email: str = None,
        preferred_email: bool = False,
        active: bool = None,
        emplid: str = None,
        discord: str = None,
    ):
        self.uid = None
        self.name = first_name + " " + middle_name + " " + last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.school_email = school_email
        self.personal_email = personal_email
        self.preferred_email = preferred_email
        self.active = active
        self.discord = discord
        self.emplid = emplid
