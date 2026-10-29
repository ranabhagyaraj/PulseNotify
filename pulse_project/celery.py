import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pulse_project.settings.local')

# Define 'celery' as the variable name so Celery can discover it
celery = Celery('pulse_project')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()