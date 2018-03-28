from django.urls import path
from django.conf.urls import url

from . import views

app_name ='bank'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
]


