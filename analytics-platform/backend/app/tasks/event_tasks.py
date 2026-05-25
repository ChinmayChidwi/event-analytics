import asyncio
import uuid

from app.core.celery_app import celery

from app.core.database import AsyncSessionLocal

from app.models.event import Event


@celery.task
def process_event_task(
    event_type,
    payload,
    organization_id
):

    asyncio.run(
        save_event(
            event_type,
            payload,
            organization_id
        )
    )


async def save_event(
    event_type,
    payload,
    organization_id
):

    async with AsyncSessionLocal() as db:

        event = Event(
            event_type=event_type,
            payload=payload,
            organization_id=uuid.UUID(
                organization_id
            )
        )

        db.add(event)

        await db.commit()

        await db.refresh(event)