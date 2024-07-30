from cryptography.fernet import Fernet, InvalidToken
import os
import unittest
from unittest.mock import patch

class Encryptor:
    def __init__(self):
        key = os.getenv('SECRET_KEY')
        if not key:
            raise ValueError("SECRET_KEY environment variable not set")
        try:
            self.key = key.encode('utf-8')
            self.cipher_suite = Fernet(self.key)
        except Exception as e:
            raise ValueError(f"Invalid SECRET_KEY format: {e}")

    def encrypt(self, plain_text: str) -> str:
        if isinstance(plain_text, str):
            plain_text = plain_text.encode('utf-8')
        return self.cipher_suite.encrypt(plain_text).decode('utf-8')

    def decrypt(self, encrypted_text: str) -> str:
        try:
            return self.cipher_suite.decrypt(encrypted_text.encode('utf-8')).decode('utf-8')
        except InvalidToken:
            raise ValueError("Invalid token or decryption failed")
