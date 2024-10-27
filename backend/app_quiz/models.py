from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # При необходимости добавьте дополнительные поля здесь
    pass

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
