from .models import *


class DataBaseManager:

    @staticmethod
    def create_budget(budget_name, month, prevision, spent):
        budget = Budget(name=budget_name, month=month, prevision=prevision, spent=spent)
        budget.save()
        return budget

    @staticmethod
    def spend_from_budget(budget, amount):
        budget.spent += amount
        budget.save()

    @staticmethod
    def spend_upcoming_from_account(account, amount):
        account.upcoming_delta -= amount
        account.save()

    @staticmethod
    def process_amount_in_account(account, amount):
        account.current_balance -= amount
        account.upcoming_delta += amount
        account.save()

    @staticmethod
    def spend_now_from_account(account, amount):
        print('balance', account.current_balance)
        account.current_balance -= amount
        account.save()
        print('balance', account.current_balance)

    @staticmethod
    def insert_operation(operation):
        operation.save()

    @staticmethod
    def check_operation(operation):
        operation.check = True
        operation.save()

    @staticmethod
    def uncheck_operation(operation):
        operation.check = False
        operation.save()

    @staticmethod
    def delete_month(month):
        month.delete()

    @staticmethod
    def delete_operation(operation):
        operation.delete()