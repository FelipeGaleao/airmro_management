from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from airmro_management.db.dao.user_dao import UserDAO
from airmro_management.db.models.user_model import UserModel
from airmro_management.web.api.user.schema import UserModelDTO, UserModelInputDTO

router = APIRouter()


@router.get("/", response_model=List[UserModelDTO])
async def get_user_model(
    limit: int = 10,
    offset: int = 0,
    user_dao: UserDAO = Depends(),
) -> List[UserModel]:
    """
    Retrieve all users from database.

    :param limit: limit of users objects, defaults to 10. \n
    :param offset: offset of users objects, defaults to 0. \n
    :param dummy_dao: DAO for users models. \n
    :return: list of users obbjects from database. \n
    """
    return await user_dao.get_all_user(limit=limit, offset=offset)


@router.post("/")
async def create_user_model(
    new_user: UserModelInputDTO,
    user_dao: UserDAO = Depends(),
) -> None:
    """
    Insert user to database
    """
    user = await user_dao.create_user(**new_user.dict())

    json_response = {
        "user_details": user,
        "message": "The user was signup with success! :)",
    }

    return json_response
