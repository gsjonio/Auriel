"""
Root router with a simple health endpoint.

:module: routers.root
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Health check")
async def health_check() -> dict:
    """
    Simple health check endpoint.

    :return: dict with status key
    """
    return {"status": "ok"}
