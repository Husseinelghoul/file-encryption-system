from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os
import base64

class SaltManager(object):
    def __init__(self, generate, path='.salt'):
        self.generate = generate
        self.path = path

    def get(self):
        if self.generate:
            return self._generate_and_store()
        return self._read()

    def _generate_and_store(self):
        salt = os.urandom(16)
        with open(self.path, 'wb') as f:
            f.write(salt)
        return salt

    def _read(self):
        with open(self.path, 'rb') as f:
            return f.read()

def derive_key(passphrase, generate_salt=False):    
    salt = bytes([0]*16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passphrase))

def encrypt(data_bytes, passphrase):
    key = derive_key(passphrase, generate_salt=True)
    f = Fernet(key)
    return f.encrypt(data_bytes)

def decrypt(data_bytes, passphrase):
    try:
        f = Fernet(derive_key(passphrase))
        return f.decrypt(data_bytes)
    except Exception as e:
        print(e)
        return False


