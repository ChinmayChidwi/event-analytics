from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.api.deps.auth import get_current_user
from app.websocket.manager import manager

from app.models.user import User
from app.tasks.event_tasks import process_event_task
from app.schemas.event import EventCreate


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("/")
async def create_event(
    request: EventCreate,
    current_user: User = Depends(get_current_user)
):

    process_event_task.delay(
        request.event_type,
        request.payload,
        str(current_user.organization_id)
    )

    await manager.broadcast({
        "event_type": request.event_type,
        "payload": request.payload
    })

    return {
        "message": "Event queued successfully"
    }