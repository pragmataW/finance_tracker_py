from authentication.exceptions import UsernameAlreadyExists
from authentication.exceptions import EmailAlreadyExists
from authentication.exceptions import WrongVerificationCode
from authentication.repo import UserRepo
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
    
    def registerUser(self, username: str, password: str, email: str):
        usernameCheck = self.repo.checkCredentialsByUsername(username)
        if usernameCheck.count() > 0:
            raise UsernameAlreadyExists("user already exists")

        emailCheck = self.repo.checkCredentialsByEmail(email)
        if emailCheck.count() > 0:
            raise EmailAlreadyExists("email already exists")
        
        encryptedPass = self.encryptor.encrypt(password)
        verificationCode = self.__createVerificationCode()
        self.repo.createUser(user_name = username, password = encryptedPass, email=email, is_verified=False, verification_code=verificationCode)

        mail = Mail(
            toMail=email,
            toName=username,
            subject="Verification Code!",
            html=f"Your verification code is {verificationCode}"
        )

        self.emailSender.sendMail(mail=mail)

    def verifyUser(self, userName: str, verificationCode: int):
        if verificationCode == self.repo.getVerificationCode(user_name=userName):
            self.repo.setIsVerified(user_name=userName, is_verified=True)
        else:
            raise WrongVerificationCode("wrong verification code")


    def isVerified(self, userName: str):
        return self.repo.getIsVerified(user_name=userName)

    def __createVerificationCode(self) -> int:
        return randint(100000, 999999)