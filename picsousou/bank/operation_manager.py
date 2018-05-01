from .budget_manager import *


def create_operation(operation):
    added = add_to_budget(operation.budget, operation.amount, operation.date)
    if added:
        if operation.payment.visible_days:
            operation.check = None

        if operation.check is False:
            DataBaseManager.spend_upcoming_from_account(operation.account, operation.amount)
        else:
            DataBaseManager.spend_now_from_account(operation.account, operation.amount)

        DataBaseManager.insert_operation(operation)


def raz_operation(operation):
    removed = remove_from_budget(operation.budget, operation.amount, operation.date)
    if removed:
        if operation.check is False:
            DataBaseManager.spend_upcoming_from_account(operation.account, -operation.amount)
        else:
            DataBaseManager.spend_now_from_account(operation.account, -operation.amount)


def delete_operation(operation):
    raz_operation(operation)
    DataBaseManager.delete_operation(operation)


def secure_check_operation(operation):
    if operation.check is False:
        DataBaseManager.process_amount_in_account(operation.account, operation.amount)
        DataBaseManager.check_operation(operation)


def secure_uncheck_operation(operation):
    if operation.check is True:
        DataBaseManager.process_amount_in_account(operation.account, -operation.amount)
        DataBaseManager.uncheck_operation(operation)
