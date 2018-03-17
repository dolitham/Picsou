from django.shortcuts import render

from .models import Operation


def index(request):
    operation_list = Operation.objects.order_by('-date')
    context = {'operation_list': operation_list}
    return render(request, 'bank/index.html', context)
