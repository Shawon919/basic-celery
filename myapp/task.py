from celery import shared_task
from time import sleep



@shared_task
def sub(x,y):
    sleep(20)
    return x - y


@shared_task
def clear_sesson_cash(id):
    print('session id is:',id)
    return id