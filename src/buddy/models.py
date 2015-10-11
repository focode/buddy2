from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from geoposition.fields import GeopositionField


class usersProfiles(models.Model):
  username = models.CharField(max_length=100)
  age = models.IntegerField(max_length=100)
  gender = models.CharField(max_length=100)
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
    boozProfileId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    Booz_shop_location = GeopositionField()
    mobile = models.IntegerField(max_length=100)
    boozshopname = models.CharField(max_length=300,blank=True, null=True)
    boozshopaddress = models.CharField(max_length=500,blank=True, null=True)
    zipcod = models.IntegerField(max_length=100,blank=True, null=True)
    datetime = models.DateTimeField("StartTime",blank=True, null=True)
    GendersAllowed = models.CharField(max_length=10,choices=genders,default=Male)
    message = models.TextField(max_length=100)


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
    GendersAllowed = models.CharField(max_length=20,choices=genders,default=Male)




