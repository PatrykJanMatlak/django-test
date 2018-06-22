from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView



var_context="Mango"
shopping_list=["Water","Apple","Candies"]

class HomeView(TemplateView):
  template_name='home.html'

  def get_context_data(self, *args, **kwargs):
    context = super(HomeView,self).get_context_data(*args, **kwargs)
    context={
    "var1":var_context,
    "shopping_list":shopping_list,
    "var2":"Verbatim test"
    }
    return context

# Create your views here.

# def home(request):
#   context={
#     "var1":var_context,
#     "shopping_list":shopping_list,
#     "var2":"Verbatim test"

#     }
#   return render(request, "home.html", context)

# def contact(request):
#   context={
#     }
#   return render(request, "contact.html", context) 

# def about(request):
#   context={
#     }
#   return render(request, "about.html", context)  

# class ContactView(TemplateView):
#   template_name='contact.html'

# class AboutView(TemplateView):
#   template_name='about.html'

