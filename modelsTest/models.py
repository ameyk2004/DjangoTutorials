from django.db import models
import datetime


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    dateCreated = models.DateField(default=datetime.date.today())
