from django.conf.urls import url
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, restaurant_createview
from django.contrib.auth.views import LoginView

urlpatterns= [
    url(r'$', RestaurantListView.as_view(), name = "list"),
    url(r'^create/$', RestaurantCreateView.as_view(), name = "create"),
    #url(r'^create/$', restaurant_createview),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name = "detail")
]