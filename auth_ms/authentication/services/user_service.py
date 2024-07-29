from authentication.repo import UserRepo
from authentication.exceptions import UsernameAlreadyExists
from authentication.exceptions import EmailAlreadyExists
from authentication.pkg import Encryptor
from authentication.pkg import EmailSender
from authentication.dto import Mail

from random import randint

class UserService: 
    repo: UserRepo
    encryptor: Encryptor
    emailSender: EmailSender

    def __init__(self):
        self.repo = UserRepo()
        self.encryptor = Encryptor()
        self.emailSender = EmailSender()
    
    def RegisterUser(self, username: str, password: str, email: str):
        usernameCheck = self.repo.checkCredentialsByUsername(username)
        if usernameCheck.count() > 0:
            raise UsernameAlreadyExists("user already exists")

        emailCheck = self.repo.checkCredentailsByEmail(email)
        if emailCheck.count() > 0:
            raise EmailAlreadyExists("email already exists")
        
        encryptedPass = self.encryptor.encrypt(password)
        verificationCode = self.__createVerificationCode()
        user = self.repo.CreateUser(user_name = username, password = encryptedPass, email=email, is_verified=False, verification_code=verificationCode)

        mail = Mail(
            toMail=email,
            toName=username,
            subject="Verification Code!",
            html=f"Your verification code is {verificationCode}"
        )

        self.emailSender.sendMail(mail=mail)
    
    def __createVerificationCode(self) -> int:
        return randint(100000, 999999)