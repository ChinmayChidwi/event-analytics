from fastapi import FastAPI
from app.core.database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.models.base import Base
from app.api.routes.users import router as users_router
from app.api.routes.events import router as events_router
from app.api.routes.analytics import (
    router as analytics_router
)
from app.websocket.routes import router as websocket_router


import app.models

from app.api.routes.auth import router as auth_router

app = FastAPI(title="Analytics Platform API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(events_router)
app.include_router(analytics_router)
app.include_router(websocket_router)


@app.get("/")
async def root():
    return {"message": "Analytics Platform Running"}