import os
import time
from datetime import datetime

from celery import Celery

backend = 'redis://127.0.0.1:6379/0'
broker = 'redis://127.0.0.1:6379/1'
celery = Celery('tasks', backend=backend, broker=broker)


@celery.task
def oadd():
    return "hello world"


@celery.task
def sleep(seconds):
    time.sleep(float(seconds))
    return seconds


@celery.task
def echo1(msg, timestamp=False):
    return "%s: %s" % (datetime.now(), msg) if timestamp else msg


@celery.task
def error(msg):
    raise Exception(msg)
