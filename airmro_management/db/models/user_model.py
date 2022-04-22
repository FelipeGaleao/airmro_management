import datetime

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP, Boolean, Integer, String

from airmro_management.db.base import Base


class UserModel(Base):
    """Model for users.
    name: str
    email: str
    password: str
    active: boolean
    createdAt: timestamp
    lastloginAt: timestamp

    """

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(length=200))
    email = Column(String(length=200), unique=True)
    password = Column(String(length=9999))
    active = Column(Boolean(), default=1)
    createdAt = Column(TIMESTAMP(), default=datetime.datetime.utcnow)
    lastLoginAt = Column(TIMESTAMP(), default=datetime.datetime.utcnow)
