import jwt
import datetime
from os import getenv


class JwtGenerator:
    def __init__(self):
        self.secretKey = getenv("JWT_KEY")

    def generateJwt(self, username: str):
        payload = {
            "user_name": username,
            "exp": datetime.datetime.now() + datetime.timedelta(days=3)
        }

        token = jwt.encode(payload=payload, key=self.secretKey, algorithm="HS256")
        return token