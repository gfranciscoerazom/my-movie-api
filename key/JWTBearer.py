from fastapi import HTTPException
from fastapi.security import HTTPBearer
from starlette.requests import Request
from .jwt_manager import decode_access_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        user_dict = decode_access_token(auth.credentials)
        if user_dict['email'] != "admin@mail.com":
            raise HTTPException(
                status_code=403,
                detail="Invalid authentication credentials.",
            )
