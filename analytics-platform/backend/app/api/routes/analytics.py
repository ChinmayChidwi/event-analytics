from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.core.database import get_db

from app.api.deps.auth import get_current_user

from app.models.user import User
from app.models.event import Event

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/summary")
async def analytics_summary(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    total_events_query = await db.execute(
        select(func.count(Event.id)).where(
            Event.organization_id ==
            current_user.organization_id
        )
    )

    total_events = total_events_query.scalar()

    return {
        "total_events": total_events
    }


@router.get("/events-by-type")
async def events_by_type(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = await db.execute(
        select(
            Event.event_type,
            func.count(Event.id)
        )
        .where(
            Event.organization_id ==
            current_user.organization_id
        )
        .group_by(Event.event_type)
    )

    rows = result.all()

    data = []

    for row in rows:

        data.append({
            "event_type": row[0],
            "count": row[1]
        })

    return data