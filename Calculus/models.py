from django.db import models


# Create your models here.
class Task1(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    power = models.PositiveSmallIntegerField(default=None)
    amperage = models.PositiveSmallIntegerField(default=None)
    scheme = models.CharField(max_length=32)
    soil = models.CharField(max_length=64)
    climate_zone = models.PositiveSmallIntegerField()


class ResultTask1(models.Model):
    diameter = models.FloatField()
    vertical_length = models.FloatField()
    num_accurate = models.FloatField()
    scheme = models.CharField(max_length=32)
    distance_between = models.FloatField()
    section = models.FloatField()
    length = models.FloatField()
    depth = models.FloatField()
    total_resistance = models.FloatField()
    normative_resistance = models.FloatField()
