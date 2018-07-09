from django.conf.urls import url
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, RestaurantUpdateView
from django.contrib.auth.views import LoginView

urlpatterns= [
    url(r'^list/$$', RestaurantListView.as_view(), name = "list"),
    url(r'^create/$', RestaurantCreateView.as_view(), name = "create"),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name = "detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name = "edit")
]