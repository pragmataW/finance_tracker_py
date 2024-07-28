from authentication.models import User

class UserRepo:
    def checkCredentials(self, username: str):
        result = User.objects.filter(user_name=username)
        return result
    
    def CreateUser(self, user_name: str, password: str): 
        user = User.objects.create(user_name = user_name, password = password)
        return user