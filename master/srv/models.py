from django.core.validators import MaxValueValidator, MinValueValidator, validate_ipv4_address, validate_integer
from django.db import models

class Unit(models.Model):
    ip = models.CharField('IP', max_length=15, validators=[validate_ipv4_address])
    port = models.IntegerField('Port', validators=[MaxValueValidator(65535), MinValueValidator(1)])

class Task(models.Model):
    input = models.CharField('Value', max_length=30)
    output = models.FloatField(null=True)
    status = models.IntegerField('Status', validators=[MaxValueValidator(2), MinValueValidator(0)],
                                 default=0)


class Thread(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='threads')
    task = models.ForeignKey(Task, models.SET_NULL, null=True)
