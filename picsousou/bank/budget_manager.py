from .database_manager import *


def find_month_containing_date_among(months, date):
    for m in months:
        if m.first_day <= date <= m.last_day:
            return m
    return False


def find_budget_linked_to_month_among(budgets, month, budget_name):
    for budget in budgets:
        if budget.month == month:
            return budget
    return DataBaseManager.create_budget(budget_name, month, 0, 0)


def add_to_budget(budget_name, amount, date):
    budgets = Budget.objects.filter(name=budget_name)
    months = Month.objects.all()
    good_month = find_month_containing_date_among(months, date)
    if not good_month:
        return False
    good_budget = find_budget_linked_to_month_among(budgets, good_month, budget_name)
    DataBaseManager.spend_from_budget(good_budget, amount)
    return True


def remove_from_budget(budget_name, amount, date):
    return add_to_budget(budget_name, -amount, date)
