from fastapi import APIRouter
from fastapi.responses import JSONResponse
from key.jwt_manager import create_access_token

from models.User import User


auth_router = APIRouter()

@auth_router.post(
    path            = "/login",
    tags            = ["Auth"],
    response_model  = dict,
    status_code     = 200,
)
def login(user: User) -> dict:
    if user.email == "admin@mail.com" and user.password == "admin":
        token: str = create_access_token(user.model_dump())
        return JSONResponse(
            content = {
                "message": "User logged in successfully.",
                "token": token,
            }
        )