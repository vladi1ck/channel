from django.db import models


# Create your models here.
class Parameter(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)