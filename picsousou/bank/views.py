from django.shortcuts import render, redirect

from .models import Operation, Account, OperationForm


def index(request):
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
        'operation_list': operation_list,
        'account_list': account_list,
        'operation_form': form}
    return render(request, 'bank/index.html', context)
