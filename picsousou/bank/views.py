from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .operation_manager import *


def index(request):
    operation_list = Operation.objects.order_by('-date')
    if request.method == 'POST':
        form = OperationForm(request.POST)
        create_operation(form.save(commit=False))
        return redirect('bank:index')
    else:
        form = OperationForm()

    context = {
        'operation_list': operation_list,
        'account_list': Account.objects.all(),
        'operation_form': form}
    return render(request, 'bank/index.html', context)


def search(request):
    operation_list = Operation.objects.all()
    operation_filter = OperationFilter(request.GET, queryset=operation_list)
    return render(request, 'bank/operation_list.html', {'filter': operation_filter})


def edit_operation(request, operation_id):
    operation = get_object_or_404(Operation, pk=operation_id)
    form = OperationForm()
    context = {
        'operation': operation,
        'form': form
    }
    return render(request, 'bank/edit_operation.html', context)
