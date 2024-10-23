from django.db import models

# Create your models here.
class UserBelajarTiga(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=1)
