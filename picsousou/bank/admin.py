from django.contrib import admin

from .models import *


class OperationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Operation._meta.get_fields()]


class BudgetAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Budget._meta.get_fields()]


admin.site.register(Account)
admin.site.register(PaymentMethod)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Person)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Month)
