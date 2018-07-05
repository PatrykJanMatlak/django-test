
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import  RestaurantLocationCreateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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


class RestaurantCreateView(LoginRequiredMixin ,CreateView):
  form_class = RestaurantLocationCreateForm
  template_name = 'restaurants/dform.html'
  login_url = '/login/'
  success_url="/restaurants/"

  def form_valid(self, form):
    instance = form.save(commit = False)
    instance.owner = self.request.user
    #instance.save()
    return super(RestaurantCreateView, self).form_valid(form)
    
@login_required(login_url='/login/')
def restaurant_createview(request):

  template_name = 'restaurants/dform.html'
  form = RestaurantLocationCreateForm(request.POST or None)
  errors = None
  
  if form.is_valid():
    if request.user.is_authenticated():
      instance = form.save(commit = False)
      instance.owner = request.user
      instance.save()
      return HttpResponseRedirect("/restaurants/")
    else:
      return HttpResponseRedirect("/about/")

  if form.errors:
    print (form.errors)
    errors = form.errors
    
  context = {"form":form, "errors":errors}

  return render(request, template_name, context)