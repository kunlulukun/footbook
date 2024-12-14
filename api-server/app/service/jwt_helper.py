import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError


class JWTHelper:
    SECRET_KEY = "your_secret_key_here"
    ALGORITHM = "HS256"

    @staticmethod
    def generate_jwt(payload: dict, expiration_days=30):
        payload = payload.copy()  # Avoid modifying the original payload
        payload["exp"] = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=expiration_days)
        token = jwt.encode(payload, JWTHelper.SECRET_KEY, algorithm=JWTHelper.ALGORITHM)
        return token

    @staticmethod
    def verify_jwt(token):
        try:
            decoded_payload = jwt.decode(token, JWTHelper.SECRET_KEY, algorithms=[JWTHelper.ALGORITHM])
            return decoded_payload
        except ExpiredSignatureError:
            raise ExpiredSignatureError("The token has expired.")
        except InvalidTokenError:
            raise InvalidTokenError("The token is invalid.")
