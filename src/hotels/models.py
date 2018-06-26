from django.db import models

# Create your models here.

class HotelOpinion(models.Model):
    name = models.CharField(max_length=120, null = False, blank = False)
    city = models.CharField(max_length=120, null = True, blank = True)
    street = models.CharField(max_length=120, null = True, blank = True)
    stars_number = models.IntegerField(verbose_name="Number of the stars:", null=True, blank = True)
    opinion =  models.TextField(max_length=400 , null = False, blank = False)

    def __str__(self):
        return self.name