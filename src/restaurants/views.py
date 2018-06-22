from django.shortcuts import render
from django.views import View



var_context="Mango"
shopping_list=["Water","Apple","Candies"]
# Create your views here.

def home(request):
  context={
    "var1":var_context,
    "shopping_list":shopping_list,
    "var2":"Verbatim test"

    }
  return render(request, "home.html", context)

def contact(request):
  context={
    }
  return render(request, "contact.html", context) 

def about(request):
  context={
    }
  return render(request, "about.html", context)  

class ContactView(View):
  def get(self, request, *args, **kwargs):
    context={
    }
    return render(request, "contact.html", context)