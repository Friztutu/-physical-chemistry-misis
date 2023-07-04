from django.db import models


# Create your models here.
class Task1(models.Model):
    # schemes
    IN_A_ROW = 0
    ALONG_THE_CONTOUR = 1

    # ZONES
    FIRST_ZONE = 1
    SECOND_ZONE = 2
    THIRD_ZONE = 3
    FOURTH_ZONE = 4

    # SOILS
    BLACK_SOIL = 1
    SANDY_LOAM = 2
    SAND = 3
    LOAM = 4
    CLAY = 5
    
    SCHEMES = (
        (IN_A_ROW, 'в ряд'),
        (ALONG_THE_CONTOUR, 'по контуру'),
    )

    ZONES = (
        (FIRST_ZONE, 'первая зона'),
        (SECOND_ZONE, 'вторая зона'),
        (THIRD_ZONE, 'третья зона'),
        (FOURTH_ZONE, 'четвертая зона'),
    )

    SOILS = (
        (BLACK_SOIL, 'чернозем'),
        (SANDY_LOAM, 'супесок'),
        (SAND, 'песок'),
        (LOAM, 'суглинок'),
        (CLAY, 'глина'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    power = models.PositiveSmallIntegerField()
    scheme = models.PositiveSmallIntegerField(choices=SCHEMES)
    soil = models.PositiveSmallIntegerField(choices=SOILS)
    climate_zone = models.PositiveSmallIntegerField(choices=ZONES)


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
