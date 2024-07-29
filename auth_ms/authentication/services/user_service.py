from authentication.repo import UserRepo
from authentication.exceptions import UsernameAlreadyExists
from authentication.exceptions import EmailAlreadyExists

class UserService: 
    repo: UserRepo

    def __init__(self):
        self.repo = UserRepo()
    
    def RegisterUser(self, username: str, password: str, email: str):
        usernameCheck = self.repo.checkCredentialsByUsername(username)
        if usernameCheck.count() > 0:
            raise UsernameAlreadyExists("user already exists")

        emailCheck = self.repo.checkCredentailsByEmail(email)
        if emailCheck.count() > 0:
            raise EmailAlreadyExists("email already exists")
    

        user = self.repo.CreateUser(user_name = username, password = password, email=email)
        return user