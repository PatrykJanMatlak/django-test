from django.shortcuts import render



var_context="Mango"
shopping_list=["Water","Apple","Candies"]
# Create your views here.
def home(request):
  context={
    "var1":var_context,
    "shopping_list":shopping_list,
    "var2":"Verbatim test"

    }
  return render(request, "base.html", context) 