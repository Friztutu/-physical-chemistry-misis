from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    TEACHER = 0
    STUDENT = 1
    STATUSES = (
        (TEACHER, 'Препод ебать'),
        (STUDENT, 'Попуск ебанные'),
    )
    group = models.CharField(max_length=32)
    status = models.PositiveSmallIntegerField(default=STUDENT, choices=STATUSES)
    student_id = models.PositiveIntegerField(blank=True, null=True)
