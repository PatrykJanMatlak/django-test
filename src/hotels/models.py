from django.db import models
from django.db.models.signals import post_save, pre_save
from .utils import unique_slug_generator, random_string_generator

# Create your models here.

class HotelOpinion(models.Model):
    name = models.CharField(max_length=120, null = False, blank = False)
    city = models.CharField(max_length=120, null = True, blank = True)
    street = models.CharField(max_length=120, null = True, blank = True)
    stars_number = models.IntegerField(verbose_name="Number of the stars:", null=True, blank = True)
    opinion =  models.TextField(max_length=400 , null = False, blank = False)
    slug = models.SlugField(null=True, blank = True)

    def __str__(self):
        return self.name

def hotel_pre_save_rec(sender, instance, *args, **kwargs):
    print("saving...")
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()


pre_save.connect(hotel_pre_save_rec, sender = HotelOpinion)