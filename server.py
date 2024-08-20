# flask server
# creates email_client instance
# just one endpoint, send email

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Wrong Endpoint"


# defaults to email all
@app.route("/email")
def hello_world(message: str, subject: str, cc: list[str] = None):
    import os
    from dotenv import load_dotenv
    from email_client import Email_Client

    load_dotenv()

    username = os.getenv("username")
    password = os.getenv("password")
    message = f"{subject}\n\n{message}"
    to = ["fahadfaruqi1@gmail.com"]

    try:
        e = Email_Client(username, password, message, subject, to)
        e.email()  # should return some result from email server
        return True
    except Exception as e:
        error_string = f"Error!: {str(e)}"
        return error_string
