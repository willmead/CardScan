from django.db import models


class Card(models.Model):
    number = models.IntegerField()
    year = models.IntegerField()
    name = models.CharField(max_length=256)
    team = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.number} - {self.name}'
