from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  collection_count = models.IntegerField(default=0)

class Collection(models.Model):
  user = models.ForeignKey(
      User,
      models.SET_NULL,
      blank=True,
      null=True,
  )
  name = models.CharField(max_length=64)
  description = models.TextField(max_length=256)
