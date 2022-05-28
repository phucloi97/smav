from django.db import models

# Create your models here.


class UserTele(models.Model):
    name = models.CharField(max_length=20)
    chat_id = models.CharField(max_length=15)


class Device(models.Model):
    name = models.CharField(max_length=25)
    imei = models.CharField(max_length=19)
