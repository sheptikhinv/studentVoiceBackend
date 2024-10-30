from fastapi import FastAPI

from helpers import ConfigHelper
from .auth import router as auth_router
from .admin import admin_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api")

is_development = ConfigHelper.get_value("is_development")

if is_development.lower() in ["true", "yes", "y"]:
    origins = [
        "*",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(admin_router)
app.include_router(auth_router)
