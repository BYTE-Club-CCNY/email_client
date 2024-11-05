import os
import pandas as pd


class CSV_To_PD:
    def __init__(self, path: str) -> None:
        self.path = path

    def try_parse(self):
        df = pd.read_csv(self.path)
        cleaned_columns = [col.strip() for col in df.columns]
        df.columns = cleaned_columns
        to_drop = [
            "Timestamp",
            "What undergraduate level are you?",
            "How long have you been coding for?",
            "What coding languages are you most proficient with? Check all that apply.",
            "Please attach a link to your GitHub profile.",
            "How would you rate your confidence in building software?",
            "Describe a memorable team experience; share challenges, your role in the group, end result, and how it impacted you.",
            "Please provide a link to a project you've done or participated in. ALTERNATIVELY: If you haven't, please describe one you would like to do.",
            "FOLLOW UP: Explain what you made/will make. What does your project aim to do, and what did you learn from it? \n\nALTERNATIVELY: Describe what you hope to learn, what the end result can look like, what steps you hope to take to get there.",
            "What career path do you plan on taking with your Computer Science degree?",
            "What do you hope to get out of the B.Y.T.E. Club?",
            "SUPPLEMENTAL: Please attach your resume below. While this will not be a major factor on your acceptance, we will take it into consideration.",
            "How would you rate your confidence in working in a team?",
            "Fahad",
            "Jawad",
            "Jinder",
            "Ishmam",
            "Thanjila",
            "Overall",
            "Statistics",
            "Accepted",
            "Denied",
            "Backburner",
            "Total",
        ]
        df.drop(to_drop, axis=1, inplace=True)

        # email based on preferred email value
        PERSONAL_EMAIL = (
            "If you prefer we contact your personal email, please put it here."
        )
        CITYMAIL = "What is your CityMail?"
        df["email"] = df[PERSONAL_EMAIL] if df[PERSONAL_EMAIL] else df[CITYMAIL]
        print(df["email"])


if __name__ == "__main__":
    """
    read a csv path from arg
    puts all of the data as inactive users into database
    """
    PATH = os.path.join(
        os.curdir, "B.Y.T.E Club Form Fall 2024 (Responses) - Form Responses 1.csv"
    )
    c = CSV_To_PD(PATH)
    c.try_parse()
