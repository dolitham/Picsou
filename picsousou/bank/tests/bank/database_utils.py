from decimal import Decimal
import datetime

from ...models import Account, PaymentMethod, BudgetName, Operation


def given_one_operation():
    Operation.objects.all().delete()

    dummy_account = Account(name='dummy account', id_name='id_name', current_balance=3987, upcoming_balance=254)
    dummy_account.save()

    dummy_payment = PaymentMethod(name='dummy payment method', account=dummy_account, visible_days=3)
    dummy_payment.save()

    dummy_budget_name = BudgetName(name='dummy budget')
    dummy_budget_name.save()

    return Operation(name='dummy operation',
                    amount=Decimal('15.33'),
                    date=datetime.date.today(),
                    budget=dummy_budget_name,
                    check=False,
                    payment=dummy_payment)


def given_one_unchecked_operation_in_db():
    operation = given_one_operation()
    operation.save()
    return operation

def given_one_checked_operation_in_db():
    Operation.objects.all().delete()

    dummy_account = Account(name='dummy account', id_name='id_name', current_balance=3987, upcoming_balance=254)
    dummy_account.save()

    dummy_payment = PaymentMethod(name='dummy payment method', account=dummy_account, visible_days=3)
    dummy_payment.save()

    dummy_budget_name = BudgetName(name='dummy budget')
    dummy_budget_name.save()

    operation =  Operation(name='dummy operation',
                    amount=Decimal('15.33'),
                    date=datetime.date.today(),
                    budget=dummy_budget_name,
                    check=True,
                    payment=dummy_payment)
    operation.save()
    return operation
