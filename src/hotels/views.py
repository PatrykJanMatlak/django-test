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

    def get_object(self, *args , **kwargs):
        hotel_name = self.kwargs.get('hotel_name')
        obj = get_object_or_404 (HotelOpinion, name = hotel_name)

        return obj

