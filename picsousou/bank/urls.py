from django.urls import path
from django.conf.urls import url

from .views import *
from .forms import *

app_name = 'bank'


urlpatterns = [
    path('', index, name='index'),
    url(r'^search/$', search, name='search'),
    path('check_operation_id/', check_operation_id, name='check_operation_id'),
    path('uncheck_operation_id/', uncheck_operation_id, name='uncheck_operation_id'),
    path('add_operation', add_operation, name='add_operation'),
    path('settings', settings, name='settings'),
    path('settings/accounts', view_accounts, name='view_accounts'),
    path('account/<int:pk>/', AccountUpdate.as_view(), name='edit_account'),
    path('settings/budgets', view_budgets, name='view_budgets'),
    path('budget/<int:pk>/', BudgetNameUpdate.as_view(), name='edit_budget'),
    path('settings/months', view_months, name='view_months'),
    path('month/<int:id_month>/', edit_month, name='edit_month'),
    path('edit_operation/<int:id_operation>/', edit_operation, name='edit_operation'),
    path('add_month', add_month, name='add_month'),
    path('monthly_budget_view/<int:id_month>/', monthly_budget_view, name='monthly_budget_view'),
    path('test_charts/<int:id_month>/', chart, name='chart_id')
]