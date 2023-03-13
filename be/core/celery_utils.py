from celery import current_app as current_celery_app

from be.core.celery_config import settings


def create_celery():
    celery_app = current_celery_app
    celery_app.config_from_object(settings, namespace='CELERY')
    celery_app.conf.update(task_track_started=True)
    celery_app.conf.update(task_serializer='json')  # selected json as we are communicating with JavaScript
    celery_app.conf.update(result_serializer='json')
    celery_app.conf.update(accept_content=['json'])
    celery_app.conf.update(result_persistent=True)
    celery_app.conf.update(worker_send_task_events=False)
    celery_app.conf.update(worker_prefetch_multiplier=1)

    return celery_app
