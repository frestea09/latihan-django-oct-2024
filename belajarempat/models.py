from django.db import models

# Create your models here.
class UserBelajarEmpat(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self) -> str:
        return self.name