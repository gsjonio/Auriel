"""
Delivery model.

:module: models.delivery
"""

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from .base import Base


class Delivery(Base):
    """
    Delivery table representing packages/encomendas.

    :param id: primary key
    :param recipient_name: name of the recipient
    :param description: optional description of the item
    :param tracking_number: optional, unique tracking identifier
    :param delivered: boolean flag whether delivered
    :param created_at: creation timestamp
    :param delivered_at: timestamp when delivered (optional)
    """

    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    recipient_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tracking_number = Column(String, nullable=True, unique=True)
    delivered = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delivered_at = Column(DateTime(timezone=True), nullable=True)
