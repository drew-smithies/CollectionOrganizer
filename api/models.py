from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

### User ###
class User(AbstractUser):
  collection_count = models.IntegerField(default=0)

### Collection ###
class Collection(models.Model):
  user = models.ForeignKey(
      User,
      models.CASCADE,
  )
  name = models.CharField(max_length=64)
  description = models.TextField(max_length=256)
  item_count = models.IntegerField(default=0)

  def __str__(self):
    return self.name

### Item ###
class Item(models.Model):
  collection = models.ForeignKey(
      Collection,
      models.CASCADE,
  )
  name = models.CharField(max_length=64)
  description = models.TextField(max_length=256)
  # Todo: add picture, notes

  def __str__(self):
    return self.name

### Category ###
class Category(models.Model):
  name = models.CharField(max_length=64)
  collection = models.ForeignKey(
      Collection,
      models.SET_NULL,
      null=True,
      blank=True,
  )

  def __str__(self):
    return self.name

### Attribute ###
class Attribute(models.Model):
  item = models.ForeignKey(
      Item,
      models.CASCADE,
  )
  category = models.ForeignKey(
      Category,
      models.SET_NULL,
      null=True,
      blank=True,
  )
  value = models.TextField(max_length=256)

  def __str__(self):
    return self.value
  