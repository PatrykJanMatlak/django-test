from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import HotelOpinion


# Create your views here.

class HotelView(ListView):
    queryset = HotelOpinion.objects.all()
    


class HotelDetailView(DetailView):
    queryset = HotelOpinion.objects.all()
