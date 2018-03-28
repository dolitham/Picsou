from django.shortcuts import render, redirect
from django import forms

from .models import Operation, Account, OperationForm
from .models import OperationFilter
from .forms import DisplayType


def index(request):
    choices = ((1, 'Normal'), (2, 'Search'), (3, 'All'))
    choices_filter = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)

    operation_list = Operation.objects.order_by('-date')
    account_list = Account.objects.order_by('-name')
    account = account_list[0]

    if request.method == 'POST':
        form = OperationForm(request.POST)
        new_operation = form.save(commit=True)
        account.balance -= new_operation.amount
        account.save()
        return redirect('bank:index')
    else:
        form = OperationForm()

    context = {
        'choices_filter' : choices_filter,
        'operation_list': operation_list,
        'account_list': account_list,
        'operation_form': form}
    return render(request, 'bank/index.html', context)


def search(request):
    form_display = DisplayType(request.POST or None)
    if request.method == "POST":
        if form_display.is_valid():
            display_type = request.POST["display_type"]
            if display_type == "Mode 1":
                return render(request, 'bank/operation_list.html', {'form': form_display})


    operation_list = Operation.objects.all()
    operation_filter = OperationFilter(request.GET, queryset=operation_list)
    return render(request, 'bank/operation_list.html', {'filter': operation_filter})