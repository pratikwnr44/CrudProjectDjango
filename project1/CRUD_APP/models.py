from django.db import models

# Create your models here.
class Order(models.Model):
    o_id = models.IntegerField()
    name = models.CharField(max_length=60)
    product = models.CharField(max_length=60)
    d_Date = models.DateField()
    add = models.CharField(max_length=60)
    price = models.FloatField()

