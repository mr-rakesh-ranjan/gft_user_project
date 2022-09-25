from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=255)
    userEmail= models.CharField(max_length=155)
    userPhone = models.CharField(max_length=10)
    userAddress = models.CharField(max_length=255)


    def __str__(self) -> str:
        return