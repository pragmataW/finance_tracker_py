from requests import post
from os import getenv
from authentication.dto import Mail


class EmailSender:
    def __init__(self):
        self.__mailUrl = getenv("MAIL_URL")

    def sendMail(self,  mail: Mail) -> int:
        headers = {
            "Content-Type": "application/json"
        }

        body = {
            "to_mail": mail.toMail,
            "to_name": mail.toName,
            "subject": mail.subject,
            "html": mail.html
        }

        response = post(url=self.__mailUrl, headers=headers, json=body)

        return response.status_code
