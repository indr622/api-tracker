from celery import Celery

from api_tracker.core.config import settings

celery_app = Celery("api_tracker", broker=settings.redis_url, backend=settings.redis_url)
