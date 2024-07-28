from authentication.repo import UserRepo
from authentication.exceptions import UsernameAlreadyExists

class UserService: 
    repo: UserRepo

    def __init__(self):
        self.repo = UserRepo()
    
    def RegisterUser(self, username: str, password: str):
        repoResult = self.repo.checkCredentials(username)

        if repoResult.count() > 0:
            raise UsernameAlreadyExists("user already exists")

        user = self.repo.CreateUser(user_name = username, password = password)
        return user