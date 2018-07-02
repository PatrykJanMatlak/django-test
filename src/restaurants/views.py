
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import RestaurantLocation
from .forms import  RestaurantLocationCreateForm
from django.http import HttpResponseRedirect


def restaurant_createview(request):
  template_name = 'restaurants/dform.html'
  form = RestaurantLocationCreateForm(request.POST or None)
  errors = None
  
  if form.is_valid():
    form.save()
    # obj = RestaurantLocation.objects.create(
    #   name = form.cleaned_data.get('name'),
    #   location = form.cleaned_data.get('location'),
    #   category = form.cleaned_data.get('category')
    #   )
    return HttpResponseRedirect("/restaurants/")

  if form.errors:
    print (form.errors)
    errors = form.errors
    
  context = {"form":form, "errors":errors}

  
  
  return render(request, template_name, context)



class RestaurantListView(ListView):
  queryset = RestaurantLocation.objects.all()
  def get_queryset(self):

    slug = self.kwargs.get("slug")
    if slug:
      queryset= RestaurantLocation.objects.filter(Q(category__icontains = slug) | Q(category__iexact = slug))
    else:
      queryset= RestaurantLocation.objects.all()
    return queryset


class RestaurantDetailView(DetailView):
  queryset = RestaurantLocation.objects.all()

  #def get_object(self, *args, **kwargs):
    #rest_id = self.kwargs.get('slug')
    #obj = get_object_or_404(RestaurantLocation, slug=rest_id) # slug = rest_id
    #return obj