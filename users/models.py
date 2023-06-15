from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Student group'
        verbose_name_plural = 'Students groups'


class CustomUser(AbstractUser):
    TEACHER = 0
    STUDENT = 1
    STATUSES = (
        (TEACHER, 'Преподаватель'),
        (STUDENT, 'Студент'),
    )

    email = models.EmailField(unique=True)
    group = models.ForeignKey(to=Group, on_delete=models.PROTECT, blank=True, null=True)
    status = models.PositiveSmallIntegerField(default=STUDENT, choices=STATUSES)
    student_id = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} | {self.last_name} | {self.group}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
