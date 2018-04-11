from django.urls import path
from django.conf.urls import url

from .views import *
from .forms import *

app_name = 'bank'



urlpatterns = [
    path('', index, name='index'),
    path('operation/<int:pk>/', OperationUpdate.as_view(), name='edit_operation'),
    url(r'^search/$', search, name='search'),
    path('add_operation', add_operation, name='add_operation'),
    path('settings', settings, name='settings')
]
