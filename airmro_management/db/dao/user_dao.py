from typing import List, Optional

import bcrypt
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from airmro_management.db.dependencies import get_db_session
from airmro_management.db.models.user_model import UserModel


class UserDAO:
    """Class for accessing user table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_user(self, name: str, email: str, password: str) -> None:
        """
        Add new Users.

        :param name: str.
        :param email: str.
        :param password: str.
        :return: user_details dict.
        """
        self.session.add(
            UserModel(
                name=name,
                email=email,
                password=bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()),
                active=1,
            ),
        )

        return {
            "name": name,
            "email": email,
        }

    async def get_all_user(self, limit: int, offset: int) -> List[UserModel]:
        """
        Get all dummy models with limit/offset pagination.

        :param limit: limit of dummies.
        :param offset: offset of dummies.
        :return: stream of dummies.
        """
        raw_dummies = await self.session.execute(
            select(UserModel).limit(limit).offset(offset),
        )

        return raw_dummies.scalars().fetchall()

    async def filter(
        self,
        name: Optional[str] = None,
    ) -> List[UserModel]:
        """
        Get specific dummy model.

        :param name: name of dummy instance.
        :return: dummy models.
        """
        query = select(UserModel)
        if name:
            query = query.where(UserModel.name == name)
        rows = await self.session.execute(query)
        return rows.scalars().fetchall()
