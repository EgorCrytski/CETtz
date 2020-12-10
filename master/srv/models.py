from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Unit(models.Model):
    ip = models.CharField('IP', max_length=15)
    port = models.IntegerField('Port', max_length=5, validators=[MaxValueValidator(65535), MinValueValidator(1)])

class Task(models.Model):
    input = models.CharField('Value', max_length=30, editable=False)
    output = models.FloatField(blank=True)
    status = models.IntegerField('Status', max_length=1, validators=[MaxValueValidator(2), MinValueValidator(0)],
                                 default=0)


class Thread(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='threads')
    task = models.ForeignKey(Task, models.SET_NULL, null=True)
