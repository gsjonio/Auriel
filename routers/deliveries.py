"""
Routers for Delivery CRUD operations.

:module: routers.deliveries
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_session
from models.delivery import Delivery
from schemas.delivery import DeliveryCreate, DeliveryOut, DeliveryUpdate

router = APIRouter(prefix="/deliveries", tags=["deliveries"])


@router.post("/", response_model=DeliveryOut, status_code=status.HTTP_201_CREATED)
async def create_delivery(
    payload: DeliveryCreate, session: AsyncSession = Depends(get_session)
) -> Delivery:
    """
    Create a new delivery record.

    :param payload: DeliveryCreate
    :param session: AsyncSession
    :return: Delivery
    """
    delivery = Delivery(**payload.dict())
    session.add(delivery)
    await session.commit()
    await session.refresh(delivery)
    return delivery


@router.get("/", response_model=List[DeliveryOut])
async def list_deliveries(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)
) -> List[Delivery]:
    """List deliveries with pagination."""
    result = await session.execute(select(Delivery).offset(skip).limit(limit))
    return result.scalars().all()


@router.get("/{delivery_id}", response_model=DeliveryOut)
async def get_delivery(
    delivery_id: int, session: AsyncSession = Depends(get_session)
) -> Delivery:
    """Get a delivery by ID."""
    result = await session.execute(select(Delivery).where(Delivery.id == delivery_id))
    delivery = result.scalar_one_or_none()
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return delivery


@router.put("/{delivery_id}", response_model=DeliveryOut)
async def update_delivery(
    delivery_id: int,
    payload: DeliveryUpdate,
    session: AsyncSession = Depends(get_session),
) -> Delivery:
    """Update an existing delivery."""
    result = await session.execute(select(Delivery).where(Delivery.id == delivery_id))
    delivery = result.scalar_one_or_none()
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(delivery, k, v)
    session.add(delivery)
    await session.commit()
    await session.refresh(delivery)
    return delivery


@router.delete("/{delivery_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery(
    delivery_id: int, session: AsyncSession = Depends(get_session)
) -> Response:
    """Delete a delivery by ID."""
    result = await session.execute(select(Delivery).where(Delivery.id == delivery_id))
    delivery = result.scalar_one_or_none()
    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")
    session.delete(delivery)
    await session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
