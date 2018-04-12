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
    path('settings', settings, name='settings'),
    path('settings/accounts', view_accounts, name='view_accounts'),
    path('account/<int:pk>/', AccountUpdate.as_view(), name='edit_account'),
    path('settings/budgets', view_budgets, name='view_budgets'),
    path('budget/<int:pk>/', BudgetNameUpdate.as_view(), name='edit_budget'),
    path('settings/payments', view_payments, name='view_payments'),
    path('payment/<int:pk>/', PaymentMethodUpdate.as_view(), name='edit_payment'),
    path('settings/months', view_months, name='view_months'),
    path('month/<int:pk>/', MonthUpdate.as_view(), name='edit_month'),

]
