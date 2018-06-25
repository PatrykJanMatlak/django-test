from django.db import models

# Create your models here.

class PubRanks(models.Model):
    name = models.CharField(max_length=120)
    location =  models.CharField(max_length=120)
    score = models.FloatField(verbose_name="Rank of the pub: ")

    def __str__(self):
        return self.name
