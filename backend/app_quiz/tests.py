from django.test import TestCase
from celery import shared_task

class SimpleTest(TestCase):
    def test(self):
        a = 1 + 1
        self.assertEqual(a, 2)  # Здесь правильное использование assertEqual
    
    def test2(self):
        a = 5
        self.assertEqual(a, 5)  # Это приведет к ошибке, т.к. a не равно 2

    def test3(self, celery_app, celery_worker):
            @celery_app.task
            def mul(x, y):
                return x * y
            celery_worker.reload()
            self.assertEqual(mul.delay(4, 4).get(timeout=10), 200)
