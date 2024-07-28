from mailjet_rest import Client
from os import getenv
from mail.dto import Mail
from dotenv import load_dotenv

class MailSender:
    def __init__(self):
        load_dotenv()

        self.__fromMail = getenv("FROM_MAIL")
        self.__mailJetKey = getenv("MAILJET_API_KEY")
        self.__mailJetSecret = getenv("MAILJET_SECRET_KEY")

    def sendMail(self, mail: Mail):
        mailJetClient = Client(auth=(self.__mailJetKey, self.__mailJetSecret), version='v3.1')
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.__fromMail,
                        "Name": "Pragma Tracker"
                },
                    "To": [
                        {
                            "Email": mail.to_mail,
                            "Name": mail.user_name
                        }
                    ],
                    "Subject": mail.subject,
                    "HTMLPart": mail.html
                }
            ]
        }

        result = mailJetClient.send.create(data=data)
        print (result.json())
        return result.status_code

