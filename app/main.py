import asyncio

import uvicorn

from .database import init_db


def start_server() -> None:
    """
    Initialize the database and start the uvicorn server
    """
    asyncio.run(init_db())
    uvicorn.run("app.routers.main:app", host="127.0.0.1", port=5001)
