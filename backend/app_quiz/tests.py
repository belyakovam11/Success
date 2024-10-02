from django.test import TestCase
from celery import shared_task

class SimpleTest(TestCase):
    def test(self):
        a = 1 + 1
        self.assertEqual(a, 2)  # Здесь правильное использование assertEqual
    
    def test2(self):
        a = 5
        self.assertEqual(a, 5)  # Это приведет к ошибке, т.к. a не равно 2

@shared_task
def add(x, y):
    return x + y