from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import ProductMark


# Create your views here.


class ProductsView(ListView):
    queryset = ProductMark.objects.all()

class ProductDetail(DetailView):
    queryset = ProductMark.objects.all()
