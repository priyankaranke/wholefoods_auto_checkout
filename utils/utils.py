import base64
import bs4
import requests

from utils.secrets import MAILGUN_API_KEY, MAILGUN_DOMAIN, EMAIL_ID


def get_decoded(input):
    base64_bytes = input.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode("ascii")


def send_email(email_message):
    return requests.post(
        "https://api.mailgun.net/v3/" + MAILGUN_DOMAIN + "/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "<YOUR NAME> @ Wholefoods Auto checkout <postmaster@" +
              MAILGUN_DOMAIN + ".mailgun.org>",
              "to": ["<YOUR NAME>", get_decoded(EMAIL_ID)],
              "subject": "Wholefoods Auto checkout service update",
              "text": email_message})
