from django.shortcuts import render

from .models import Operation, Account


def index(request):
    operation_list = Operation.objects.order_by('-date')
    account_list = Account.objects.order_by('-name')
    context = {
        'operation_list': operation_list,
        'account_list' : account_list }
    return render(request, 'bank/index.html', context)