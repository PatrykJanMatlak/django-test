from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import RestaurantLocation


def restaurant_listview(request):
  template_name="restaurants/restaurants_list.html"
  
  queryset = RestaurantLocation.objects.all()

  context={
    "list1":queryset

  }
  return render(request, template_name ,context)


