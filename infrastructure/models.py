from django.db import models

class Bed(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name
