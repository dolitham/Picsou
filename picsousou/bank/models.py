from django.db import models
from django.utils.timezone import now

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


class Operation(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField('Date', default=now())
    budget = models.CharField(max_length=15, choices=BUDGET_CHOICES, default=HB)


class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
