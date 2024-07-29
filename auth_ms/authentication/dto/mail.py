class Mail:
    def __init__(self, toMail: str, toName: str, subject: str, html: str):
        self.toMail = toMail
        self.toName = toName
        self.subject = subject
        self.html = html