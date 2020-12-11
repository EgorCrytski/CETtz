from celery import Celery
import math

celery = Celery()

@celery.task
def calculate(num):
    return math.sqrt(num)

celery.worker_main()