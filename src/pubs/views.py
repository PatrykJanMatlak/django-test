from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import PubRanks


def pubs_view(request):
  template_name="pubs/pubs_list.html"
  
  queryset = PubRanks.objects.all()

  context={
    "list1":queryset

  }
  return render(request, template_name ,context)


