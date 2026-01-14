"""
Application entrypoint.

:module: main
"""

from fastapi import FastAPI

from routers.root import router as root_router

app = FastAPI(title="Test Project")

app.include_router(root_router)
