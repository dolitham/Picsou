from .budget_manager import *


def create_operation(operation):
    added = add_to_budget(operation.budget, operation.amount, operation.date)
    if added:
        DataBaseManager.spend_from_account(operation.account, operation.amount)
        DataBaseManager.insert_operation(operation)
    if operation.check:
        check_operation(operation)


def check_operation(operation):
    if not operation.check:
        DataBaseManager.process_amount_in_account(operation.account, operation.amount)
        DataBaseManager.check_operation(operation)


def uncheck_operation(operation):
    if operation.check:
        DataBaseManager.process_amount_in_account(operation.account, -operation.amount)
        DataBaseManager.uncheck_operation(operation)
