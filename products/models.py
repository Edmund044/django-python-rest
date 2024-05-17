from django.db import models

class Product(models.Model):
  product_name = models.CharField(max_length=255)
  product_description = models.CharField(max_length=255,default='')
  product_image =  models.CharField(max_length=255,default='')
  price = models.IntegerField(default=0)
  reviews = models.CharField(max_length=255,default='')
  shipping_rates = models.IntegerField(default=0)
  # delivery_timelines = models.CharField(max_length=255)
  # return_timelines = models.CharField(max_length=255)

