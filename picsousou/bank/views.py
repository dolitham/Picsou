from django.shortcuts import render, redirect
from .forms import *
from .operation_manager import *


def index(request):
    operation_list = Operation.objects.filter(check=False).order_by('-date')
    operation_list = [op for op in operation_list if op.is_recent_or_pending()]

    context = {
        'operation_list': operation_list,
        'account_list': Account.objects.all()}
    return render(request, 'bank/index.html', context)


def search(request):
    operation_list = Operation.objects.all()
    operation_filter = OperationFilter(request.GET, queryset=operation_list)
    return render(request, 'bank/search_operation.html', {'filter': operation_filter})


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
