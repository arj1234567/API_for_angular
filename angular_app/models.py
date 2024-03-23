from django.db import models
class Userdata_tb(models.Model):
    Full_name = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
# Create your models here.
