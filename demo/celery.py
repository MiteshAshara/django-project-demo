import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

app = Celery('demo')

# Set the broker URL to localhost
app.conf.broker_url = 'amqp://guest:guest@localhost:5672//'

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
app.conf.imports = ['demo.task']
app.conf.result_expires = 3600   

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')