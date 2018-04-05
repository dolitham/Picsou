from django.contrib import admin

from .models import *

def get_all_fields_from(model):
    return [f.name for f in model._meta.get_fields() if f.auto_created == False]


class OperationAdmin(admin.ModelAdmin):
    list_display = get_all_fields_from(Operation)

class BudgetAdmin(admin.ModelAdmin):
    list_display = get_all_fields_from(Budget)

class MonthAdmin(admin.ModelAdmin):
    list_display = get_all_fields_from(Month)


admin.site.register(BudgetName)
admin.site.register(Account)
admin.site.register(PaymentMethod)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Person)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Month, MonthAdmin)
