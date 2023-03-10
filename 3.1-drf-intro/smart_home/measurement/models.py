from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)