from rest_framework import serializers

class Mail:
    def __init__(self, subject: str, html: str, to_mail: str, user_name: str):
        self.subject = subject
        self.html = html
        self.to_mail = to_mail
        self.user_name = user_name
