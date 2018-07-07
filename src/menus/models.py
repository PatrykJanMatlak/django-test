from django.db import models
from django.conf import settings
from restaurants.models import RestaurantLocation
from django.core.urlresolvers import reverse
# Create your models here.

class Item(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant  = models.ForeignKey(RestaurantLocation)
    
    name        = models.CharField(max_length=120)
    contents    = models.TextField(help_text = 'separate each item by comma')
    excludes    = models.TextField(help_text = 'separate each item by comma', null = True, blank = True)
    public      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse ("menus:detail", kwargs = {"pk":self.pk})

    class Meta:
        ordering = ['-updated','-created']

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")
    
    def __str__(self):
        return self.name