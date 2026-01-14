"""
Application entrypoint.

:module: main
"""

from fastapi import FastAPI

from routers.deliveries import router as deliveries_router
from routers.root import router as root_router

app = FastAPI(title="Auriel")

app.include_router(root_router)
app.include_router(deliveries_router)
