<<<<<<< HEAD
from  celery import shared_task
@shared_task(bind=True)
def test_fun(self):
    for i in range(10):
        print(i)
    return "done"


=======
from  celery import shared_task
@shared_task(bind=True)
def test_fun(self):
    for i in range(10):
        print(i)
    return "done"


>>>>>>> 550c397da82c84627a5a585ea40baaaeb7077ad9
