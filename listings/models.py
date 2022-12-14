from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
  realtor = models.OneToOneField(Realtor, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  district = models.CharField(max_length=200)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title


