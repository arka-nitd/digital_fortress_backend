from base.models import BaseModel
from django.db import models
from users.models import User


class Round(BaseModel):

    BASE = 0

    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return str(self.number)


class LeaderBoard(BaseModel):

    user = models.OneToOneField(User)
    round = models.ForeignKey(Round)


class Hint(BaseModel):

    round = models.ForeignKey(Round)
    title = models.CharField(max_length=100)
    detail = models.TextField(max_length=500)


class Question(BaseModel):

    number = models.IntegerField()
    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=1000)
    answer = models.CharField(max_length=50)
    round = models.ForeignKey(Round)
    position = models.CharField(max_length=100)
