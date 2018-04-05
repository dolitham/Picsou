import django_filters
from django.forms import ModelForm
from django.views.generic import UpdateView

from .models import *


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['name', 'amount']


class OperationFilter(django_filters.FilterSet):
    class Meta:
        model = Operation
        fields = {
            'name': ['exact', 'icontains', ],
            'amount': ['lt', 'gt', ],
            'date': ['lt', 'gt', ],
        }


class OperationUpdate(UpdateView):
    model = Operation
    fields = ['name', 'amount']
    template_name = 'bank/edit_operation.html'
    success_url = '/bank/'
