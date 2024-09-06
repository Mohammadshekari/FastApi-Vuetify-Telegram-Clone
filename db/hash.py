from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:
    value: str = None

    def __init__(self, value) -> None:
        self.value = value

    def bcrypt(self):
        return pwd_ctx.hash(self.value)

    def verify(self, hash_value):
        return pwd_ctx.verify(self.value, hash_value)
