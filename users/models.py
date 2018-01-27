from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import BaseModel


class User(AbstractUser, BaseModel):
    avatar = models.URLField(default="http://lorempixel.com/200/200/?random")
