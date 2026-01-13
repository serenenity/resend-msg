import os
import resend
from dotenv import load_dotenv

load_dotenv()

if not os.environ["RESEND_API_KEY"]:
    raise EnvironmentError["ESEND_API_KEY is missing"]

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email():
    try:
        email = resend.Emails.send({
            "from": "Welcome <paulmike@contact.moneysense.ng>",
            "to": "stephenmatthew283@gmail.com",
            "subject": "Hello World",
            "html": "<p>Welcome to Moneysense Inc.<strong> We are just getting started</strong>!</p>"
        })
        print("Email sent successfully:", email)
    except Exception as e:
        print("Error sending email:", e)

if __name__ == "__main__":
    send_email()