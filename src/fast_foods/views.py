from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import FastFoodScore

# Create your views here.


def ff_listview(request):
  template_name="fast_foods/ff_list.html"
  
  queryset2 = FastFoodScore.objects.all()

  context={
    "list2":queryset2

  }
  return render(request, template_name ,context)
