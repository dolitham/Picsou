from copy import deepcopy

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .operation_manager import *
from .month_manager import *
from .fusioncharts import FusionCharts
from .json_maker import *


def settings(request):
    account_list = Account.objects.all()
    url = request.get_full_path()
    context = {
        'account_list': account_list,
        'current_url': url
    }
    return render(request, 'bank/settings.html', context)


def index(request):
    operation_list = Operation.objects.exclude(check=True).order_by('-date')
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
        operation_list = Operation.objects.all().order_by('-id')[:10]
    operation_filter = OperationFilter(request.GET, queryset=operation_list)
    total_operations = OperationFilter(request.GET, queryset=operation_list).qs.aggregate(Sum('amount'))
    context = {
        'filter': operation_filter,
        'total': total_operations['amount__sum']
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


def edit_operation(request, id_operation):
    former_operation = get_object_or_404(Operation, id=id_operation)
    form = OperationForm(request.POST or None, instance=deepcopy(former_operation))
    context = {
        'form': form,
    }

    if form.is_valid():
        if 'delete' in request.POST:
            delete_operation(former_operation)
            return redirect('bank:index')

        raz_operation(former_operation)
        create_operation(form.save(commit=False))
        return redirect('bank:index')

    return render(request, 'bank/edit_operation.html', context)


def edit_month(request, id_month):
    month = get_object_or_404(Month, id=id_month)
    form = MonthForm(request.POST or None, instance=month)
    context = {
        'form': form,
        'delete': True
    }
    if form.is_valid():
        if 'delete' in request.POST:
            deleted, nb_operations = delete_month(month)
            if deleted:
                return redirect('bank:view_months')
            else:
                context['text'] = str(nb_operations)+' operations during this month'
        else:
            form.save(commit=True)
            return redirect('bank:view_months')
    return render(request, 'bank/edit_settings.html', context)


def add_month(request):
    form = MonthForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        month = form.save(commit=False)
        created, overlap_months = create_month(month)
        if created:
            return redirect('bank:view_months')
        else:
            context['text'] = 'OVERLAP AVEC '
            context['list'] = overlap_months

    return render(request, 'bank/edit_settings.html', context)


def monthly_budget_view(request, id_month):
    month = get_object_or_404(Month, id=id_month)
    budgets = Budget.objects.filter(month=month)
    context = {
        'budgets' : budgets,
        'month_name' : month.id_name
    }
    return render(request, 'bank/monthly_budget_view.html', context)


def chart(request, id_month):
    month = get_object_or_404(Month, id=id_month)
    budgets = Budget.objects.filter(month=month).order_by('-prevision')
    json_string_budgets = json_maker(budgets)
    column2d = FusionCharts("stackedbar2d", "ex1", "600", "400", "chart-1", "json", json_string_budgets)
    context = {
        'output': column2d.render(),
        'month_name' : month.id_name
    }
    print(json_string_budgets)
    return render(request, 'bank/fusioncharts-html-template.html', context)