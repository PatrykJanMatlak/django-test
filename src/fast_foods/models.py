from django.db import models

# Create your models here.

class FastFoodScore(models.Model):
    name = models.CharField(max_length=120, null = False, blank = False)
    location = models.CharField(max_length=120, null=True , blank = True)
    timestamp =  models.DateTimeField(auto_now_add=True, auto_now=False)
    score = models.FloatField(verbose_name="Your score:", null=False)