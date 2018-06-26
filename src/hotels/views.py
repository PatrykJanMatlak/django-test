from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import HotelOpinion


# Create your views here.

class HotelView(ListView):
    template_name ="hotels/hotel-list.html"
    queryset = HotelOpinion.objects.all()
    