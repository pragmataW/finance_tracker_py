from authentication.models import User

class UserRepo:
    def checkCredentialsByUsername(self, username: str):
        result = User.objects.filter(user_name=username)
        return result
    
    def checkCredentialsByEmail(self, email: str):
        result = User.objects.filter(email=email)
        return result
    
    def createUser(self, user_name: str, password: str, email: str, is_verified: bool, verification_code: int): 
        user = User.objects.create(
            user_name=user_name, 
            password=password, 
            email=email, 
            is_verified=is_verified, 
            verification_code=verification_code
        )
        return user

    def getIsVerified(self, user_name: str) -> bool:
        user = User.objects.filter(user_name=user_name).first()
        if user:
            return user.is_verified
        return False
    
    def setIsVerified(self, user_name: str, is_verified: bool) -> bool:
        user = User.objects.filter(user_name=user_name).first()
        if user:
            user.is_verified = is_verified
            user.save()
            return True
        return False
    
    def getVerificationCode(self, user_name: str) -> int:
        user = User.objects.filter(user_name=user_name).first()
        if user:
            return user.verification_code
        return None