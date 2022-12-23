from datetime import datetime, timedelta
from django.core.signing import Signer, BadSignature

class TokenEncrypter:
    """Provided utilities to encrypt and decrypt tokens"""

    def __init__(self):
        self.date_format = "%Y-%m-%d %H"

    def encrypt_user_token(self, token: str, ttl: int = 1) -> str:
        """
        Returns a user token encrypted.

            Parameters:
                token (str): A decrypted token
                ttl (int): Time to live the token in hours
        """
        signer = Signer()
        date_to_expire = datetime.now() + timedelta(hours=ttl)
        date_to_expire_converted = date_to_expire.strftime(self.date_format)
        raw_user_token = {
            'token': token,
            'ttl': date_to_expire_converted
        }
        return signer.sign_object(raw_user_token)

    def decrypt_user_token(self, encrypted_token: str) -> dict[str, str]:
        """
        Returns a dictionary with token or error message
        """
        try:
            signer = Signer()
            decrypted_object = signer.unsign_object(encrypted_token)
            now_date = datetime.now()
            date_to_expire = datetime.strptime(decrypted_object["ttl"], self.date_format)
            if now_date > date_to_expire:
                return {"error": "Token has expired, please login again..."}
            return {"token": decrypted_object["token"]}
        except BadSignature as e:
            return {"error": "Token is invalid, please log in again..."}
