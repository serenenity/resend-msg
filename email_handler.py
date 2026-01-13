import os
import resend
from dotenv import load_dotenv

load_dotenv()

if not os.environ["RESEND_API_KEY"]:
    raise EnvironmentError["ESEND_API_KEY is missing"]

resend.api_key = os.getenv("RESEND_API_KEY")


def send_email(sender, to, subject, content):
    try:
        email = resend.Emails.send({
            "from": sender,
            "to": to,
            "subject": subject,
            "html": content
        })
        print("Email sent successfully:", email)
    except Exception as e:
        print("Error sending email:", e)

if __name__ == "__main__":
    send_email(
        "Welcome <paulmike@contact.moneysense.ng>",
        "oderamark120@gmail.com",
        "Hello World",
        "<p>Welcome to Moneysense Inc.<strong> We are just getting started</strong>!</p>"
    )