from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import RestaurantLocation


list1=[1,2,3]

def restaurant_listview(request):
  template_name="restaurants/restaurants_list.html"
  try:
    queryset = RestaurantLocation.objects.all()
  except:
    pass
  context={
    "list1":queryset

  }
  return render(request, template_name ,context)


