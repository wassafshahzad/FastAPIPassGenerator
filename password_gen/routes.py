from .service import generate_pass
from constant import MIN_LENGTH, PASSWORD_PATH
from fastapi import APIRouter, Query
from .model import Password

router = APIRouter()


@router.get(PASSWORD_PATH, response_model=Password)
async def get_password(length: int = Query(MIN_LENGTH, ge=MIN_LENGTH)):
    return generate_pass(length)
