from django.http import HttpResponse
from django.shortcuts import render



var_context="Mango"
# Create your views here.
def home(request):
  return render(request, "base.html", {"var1":var_context}) 