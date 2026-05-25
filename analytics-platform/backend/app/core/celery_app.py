from celery import Celery

celery = Celery(
    "analytics_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=[
        "app.tasks.event_tasks"
    ]
)

celery.conf.task_routes = {
    "app.tasks.event_tasks.process_event_task": {
        "queue": "events"
    }
}