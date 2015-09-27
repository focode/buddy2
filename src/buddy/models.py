from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class usersProfiles(models.Model):
  username = models.CharField(max_length=100)
  age = models.IntegerField(max_length=100)
  email = models.EmailField()
  gender = models.CharField(max_length=100)
  address = models.TextField(max_length=500)
  ethenic = models.CharField(max_length=100)
  interest = models.TextField(max_length=500)

class boozProfiles(models.Model):
    Male = 'Male'
    Female = 'Female'
    Others = 'Others'

    genders = (

    (Male, 'Male'),
    (Female, 'FeMale'),
    (Others, 'Others')
      )
    boozshopname = models.CharField(max_length=300)
    boozshopaddress = models.CharField(max_length=500)
    zipcod = models.IntegerField(max_length=100)
    datetime = models.DateTimeField("StartTime")
    GendersAllowed = models.CharField(max_length=2,choices=genders,default=Male)
    message = models.CharField(max_length=100)
    long_position   = models.DecimalField (max_digits=8, decimal_places=3)
    lat_position   = models.DecimalField (max_digits=8, decimal_places=3)
    mobile = models.IntegerField(max_length=100)


class locateDrinkers(models.Model):
    Male = 'Male'
    Female = 'Female'
    Others = 'Others'

    genders = (

    (Male, 'Male'),
    (Female, 'FeMale'),
    (Others, 'Others')
      )
    boozshopname = models.CharField(max_length=300)
    boozshopaddress = models.CharField(max_length=500)
    interests = models.CharField(max_length=500)
    zipcod = models.IntegerField(max_length=100)
    datetime = models.DateTimeField("StartTime")
    GendersAllowed = models.CharField(max_length=2,choices=genders,default=Male)




