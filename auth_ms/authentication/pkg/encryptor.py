from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.chiperSuit = Fernet(self.key)

    def encrypt(self, plainText: str) -> str:
        if isinstance(plainText, str):
            plainText = plainText.encode('utf-8')
        return self.chiperSuit.encrypt(plainText).decode('utf-8')

    def decrypt(self, encryptedText: str) -> str:
        encryptedText = encryptedText.encode('utf-8')
        decryptedText = self.chiperSuit.decrypt(encryptedText).decode('utf-8')
        return decryptedText