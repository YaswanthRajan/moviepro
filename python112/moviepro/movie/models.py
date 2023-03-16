from django.db import models


# Create your models here.
class ko(models.Model):
    name = models.CharField(max_length=30)
    des = models.TextField()
    year = models.DateField()
    image = models.ImageField(upload_to='img')
