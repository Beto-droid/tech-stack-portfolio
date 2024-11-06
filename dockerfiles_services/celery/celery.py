from celery import Celery
app = Celery('your_project', broker='redis://redis:6379/0')
@app.task
def hello():
    return 'Hello, World!'
