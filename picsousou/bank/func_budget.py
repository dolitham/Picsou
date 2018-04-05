from .models import *


def add_to_budget(name, amount, date):
    budgets = Budget.objects.filter(name=name)
    good_budget = [b for b in budgets if b.month.first_day <= date <= b.month.last_day]
    if good_budget:
        budget = good_budget[0]
        budget.spent += amount
        budget.save()
        return True
    else:
        return False
