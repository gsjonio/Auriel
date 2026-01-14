"""
Example SQLAlchemy model for demonstration.

:module: models.user
"""

from sqlalchemy import Column, Integer, String

from .base import Base


class User(Base):
    """
    Minimal User model.

    :param id: primary key
    :param username: unique username
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
