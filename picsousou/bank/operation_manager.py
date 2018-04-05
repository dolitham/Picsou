from .database_manager import *
from .budget_manager import *


def create_operation(operation):
    account = operation.payment.account
    amount = operation.amount
    budget_name = operation.budget
    date = operation.date
    added = add_to_budget(budget_name, amount, date)
    if added:
        DataBaseManager.spend_from_account(account, amount)
        DataBaseManager.insert_operation(operation)