from django.urls import path
from .views import reroute, shorten_url


app_name = 'shorten'


urlpatterns = [
    path('', shorten_url, name='create'),
    path('<str:shortened_id>', reroute, name='reroute')
]