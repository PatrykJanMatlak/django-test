from django.db import models
from datetime import datetime
from .utils import *
from django.db.models.signals import post_save, pre_save


# Create your models here.
class ProductMark(models.Model):
    name = models.CharField(max_length=120, null =  False, blank = False)
    price = models.FloatField(verbose_name = "Price of the product, count in PLN!")
    opinion = models.TextField(max_length = 400 ,verbose_name = "Your opinion goes here...")
    score = models.FloatField(verbose_name= "Your mark of the product. From 1 to 10.")
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(null = True, blank = True)

    def __str__(self):
        return self.name


def product_slug_receiver(sender, instance, *args, **kwargs ):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

pre_save.connect(product_slug_receiver, sender = ProductMark)