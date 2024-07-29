from authentication.models import User

class UserRepo:
    def checkCredentialsByUsername(self, username: str):
        result = User.objects.filter(user_name=username)
        return result
    
    def checkCredentailsByEmail(self, email: str):
        result = User.objects.filter(email=email)
        return result
    
    def CreateUser(self, user_name: str, password: str, email: str): 
        user = User.objects.create(user_name = user_name, password = password, email=email)
        return user