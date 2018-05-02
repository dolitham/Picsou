import django_filters
from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, DateInput
from django.views.generic import UpdateView

from .models import *


EDIT_SETTINGS_HTML = 'bank/edit_settings.html'


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['name', 'amount', 'budget', 'payment', 'check', 'date']
        widgets = {'check': CheckboxInput(), 'date': DateInput(attrs={'type':'date', 'class':'datepicker'})}


class OperationFilter(django_filters.FilterSet):
    class Meta:
        model = Operation
        fields = {
            'name': ['exact', 'icontains', ],
            'amount': ['lt', 'gt', ],
            'date': ['lt', 'gt', ],
            'budget' : ['exact']
        }


class AccountUpdate(UpdateView):
    model = Account
    fields = ['name']
    template_name = EDIT_SETTINGS_HTML
    success_url = '/bank/settings/accounts'


class BudgetNameUpdate(UpdateView):
    model = BudgetName
    fields = ['name']
    template_name = EDIT_SETTINGS_HTML
    success_url = '/bank/settings/budgets'


class MonthForm(ModelForm):
    class Meta:
        model = Month
        fields = ['first_day', 'last_day']


class MonthUpdate(UpdateView):
    model = Month
    fields = ['first_day', 'last_day']
    template_name = EDIT_SETTINGS_HTML
    success_url = '/bank/settings/months'
