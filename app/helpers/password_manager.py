import random
import string

from passlib.context import CryptContext


class PasswordManager:
    """
    All required functions to work with passwords
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """
        Hashes password with bcrypt and giving hash in return
        :param password:
        :return: hash of given password
        """
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies password by hashing it again and comparing with existing hash
        :param plain_password: Password to verify
        :param hashed_password: Hashed user password
        :return: True if password is correct else False
        """
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_random_password(cls, size: int = 8, chars: str = string.ascii_uppercase + string.digits) -> str:
        """
        Generates a random password of given size with given chars
        :param size: Length of new password
        :param chars: Characters to use in password
        :return: string with random password
        """
        return ''.join(random.choice(chars) for _ in range(size))
