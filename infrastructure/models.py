from django.db import models

class Bed(models.Model):
    bed_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    last_maintenance_date = models.DateField()