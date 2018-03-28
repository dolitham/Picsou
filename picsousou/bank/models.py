from django.db import models
from django.utils.timezone import now
from django.forms import ModelForm
import django_filters

RE = "Restos"
MA = 'Market'
CH = 'Charges'
HB = 'HB'

BUDGET_CHOICES = (
    (RE, 'Restos'),
    (MA, 'Market'),
    (CH, 'Charges'),
    (HB, 'Hors Budget')
)


class Month(models.Model):
    first_day = models.DateField('First Day')
    last_day = models.DateField('Last Day')
    total_input = models.DecimalField(max_digits=7, decimal_places=2, default = 0)
    total_output = models.DecimalField(max_digits=7, decimal_places=2, default = 0)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default = 0)


class Operation(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField('Date', default=now())
    budget = models.CharField(max_length=15, choices=BUDGET_CHOICES, default=HB)


class OperationFilter(django_filters.FilterSet):
    class Meta:
        model = Operation
        fields = {
            'name': ['exact', 'icontains',],
            'amount': ['lt', 'gt' ],
            'date': ['lt', 'gt' ],
            'budget': ['exact', ],
        }


class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=7, decimal_places=2)


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['name', 'amount']
