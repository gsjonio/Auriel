"""
Pydantic schemas for Delivery.

:module: schemas.delivery
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DeliveryBase(BaseModel):
    """
    Shared fields for Delivery.

    :param recipient_name: name of the recipient
    :param description: optional description
    :param tracking_number: optional tracking id
    """

    recipient_name: str
    description: Optional[str] = None
    tracking_number: Optional[str] = None


class DeliveryCreate(DeliveryBase):
    """Schema for creating a delivery."""


class DeliveryUpdate(BaseModel):
    """Schema for updating a delivery."""

    recipient_name: Optional[str] = None
    description: Optional[str] = None
    tracking_number: Optional[str] = None
    delivered: Optional[bool] = None


class DeliveryOut(DeliveryBase):
    """Schema returned in responses."""

    id: int
    delivered: bool
    created_at: datetime
    delivered_at: Optional[datetime] = None

    class Config:
        orm_mode = True
