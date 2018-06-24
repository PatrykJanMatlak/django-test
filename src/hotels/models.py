from django.db import models

# Create your models here.

class HotelOpinion(models.Model):
    name = models.CharField(max_length=120, null = False, blank = False)
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.name