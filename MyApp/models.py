from django.contrib.admin.helpers import AdminForm
from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    otp=models.IntegerField(default=4567)


class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    qty =models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)

class images(models.Model):
    image_url = models.FileField(upload_to='media/images/')
