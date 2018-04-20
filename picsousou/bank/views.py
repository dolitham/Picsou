from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .operation_manager import *


def settings(request):
    account_list = Account.objects.all()
    url = request.get_full_path()
    context = {
        'account_list': account_list,
        'current_url': url
    }
    return render(request, 'bank/settings.html', context)


def index(request):
    operation_list = Operation.objects.filter(check=False).order_by('-date')
    operation_list = [op for op in operation_list if op.is_recent_or_pending()]

    context = {
        'operation_list': operation_list,
        'account_list': Account.objects.all()
    }
    return render(request, 'bank/index.html', context)


def search(request):
    req = request.GET
    if [req[u] for u in req]:
        operation_list = Operation.objects.all()
    else:
        operation_list = Operation.objects.filter(amount__lte=-1000)
        operation_list = operation_list.exclude(amount__lte=-1000)
    operation_filter = OperationFilter(request.GET, queryset=operation_list)
    total_operations = OperationFilter(request.GET, queryset=operation_list).qs.aggregate(Sum('amount'))
    context = {
        'filter': operation_filter,
        'total' : total_operations['amount__sum']
    }
    return render(request, 'bank/search_operation.html', context)


def add_operation(request):
    if request.method == 'POST':
        form = OperationForm(request.POST)
        create_operation(form.save(commit=False))
        if 'add_another' in request.POST:
            return redirect('bank:add_operation')
        elif 'return' in request.POST:
            return redirect('bank:index')
    else:
        form = OperationForm()

    context = {
        'operation_form': form}
    return render(request, 'bank/add_operation.html', context)


def view_accounts(request):
    account_list = Account.objects.all()
    context = {
        'account_list': account_list
    }
    return render(request, 'bank/view_accounts.html', context)


def view_budgets(request):
    budget_list = BudgetName.objects.all()
    context = {
        'budget_list': budget_list
    }
    return render(request, 'bank/view_budgets.html', context)


def view_months(request):
    month_list = Month.objects.all()
    context = {
        'month_list': month_list
    }
    return render(request, 'bank/view_months.html', context)


def view_payments(request):
    payment_list = PaymentMethod.objects.all()
    context = {
        'payment_list': payment_list
    }
    return render(request, 'bank/view_payments.html', context)


def check_operation_id(request):
    operation_id = request.GET['operation_id']
    operation = Operation.objects.get(pk=operation_id)
    secure_check_operation(operation)
    return HttpResponse('hello')


def uncheck_operation_id(request):
    operation_id = request.GET['operation_id']
    operation = Operation.objects.get(pk=operation_id)
    secure_uncheck_operation(operation)
    return HttpResponse('hello')


def my_view(request, id_operation):
    instance = get_object_or_404(Operation, id=id_operation)
    form = OperationForm(request.POST or None, instance=instance)
    former_operation = Operation.objects.get(pk=id_operation)
    context = {
        'form': form,
        'text':'youpla '
    }
    if form.is_valid():
        raz_operation(former_operation)
        create_operation(form.save(commit=False))
        return redirect('bank:index')
    return render(request, 'bank/edit_operation.html', context)
