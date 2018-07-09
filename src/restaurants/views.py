
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from .forms import  RestaurantLocationCreateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class RestaurantListView(LoginRequiredMixin,ListView):
  def get_queryset(self):
    return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin,DetailView):
  def get_queryset(self):
    return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin ,CreateView):
  form_class = RestaurantLocationCreateForm
  template_name = 'restaurants/dform.html'
  
  success_url="/restaurants/list"

  def form_valid(self, form):
    instance = form.save(commit = False)
    instance.owner = self.request.user
    #instance.save()
    return super(RestaurantCreateView, self).form_valid(form)

  def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title']= "add restaurant"
        return context

class RestaurantUpdateView(LoginRequiredMixin ,CreateView):
  form_class = RestaurantLocationCreateForm
  template_name = 'form.html'
  
  success_url="/restaurants/list"

  def form_valid(self, form):
    instance = form.save(commit = False)
    instance.owner = self.request.user
    #instance.save()
    return super(RestaurantUpdateView, self).form_valid(form)
  
  def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title']= "edit restaurant"
        return context
    