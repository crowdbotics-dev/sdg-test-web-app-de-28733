from django.conf import settings
from django.db import models


class Resource(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    rate = models.FloatField()


class Task(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    resource = models.IntegerField()
