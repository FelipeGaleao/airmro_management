from datetime import datetime

from pydantic import BaseModel


class UserModelDTO(BaseModel):
    """
    DTO for user models.

    It returned when accessing user models from the API.
    """

    id: int
    name: str
    email: str
    active: bool
    createdAt: datetime
    lastLoginAt: datetime

    class Config:
        orm_mode = True


class UserModelInputDTO(BaseModel):
    """DTO for creating new user model."""

    name: str
    password: str
    email: str
