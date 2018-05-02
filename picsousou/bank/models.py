from django.db import models
import datetime
from decimal import *


class Month(models.Model):
    first_day = models.DateField('First Day')
    last_day = models.DateField('Last Day')
    total_input = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_output = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    @property
    def is_current(self):
        return self.first_day <= datetime.today() <= self.last_day

    @property
    def nb_days(self):
        days = self.last_day - self.first_day
        return days.days+1

    @property
    def id_name(self):
        middle_date = self.first_day + datetime.timedelta(days=self.nb_days//2)
        return middle_date.strftime("%b %Y")

    @property
    def month_progress(self):
        today = datetime.date.today()
        if today > self.last_day:
            return 1
        if today < self.first_day:
            return 0
        days_spent = today - self.first_day
        days_spent = days_spent.days + 1
        return days_spent / self.nb_days

    def __str__(self):
        return str(self.id_name)


class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_name = models.CharField(max_length=50)
    payment_name = models.CharField(max_length=15)
    instant_payment = models.BooleanField(default=False)
    nb_days_operations_remain_visible = models.IntegerField(default=0)
    #initial_balance = models.DecimalField(max_digits=7, decimal_places=2, editable=False)
    #initial_delta = models.DecimalField(max_digits=7, decimal_places=2, editable=False)
    current_balance = models.DecimalField(max_digits=7, decimal_places=2)
    upcoming_delta = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.payment_name

    @property
    def upcoming_balance(self):
        return self.current_balance + self.upcoming_delta


class BudgetName(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Budget(models.Model):
    name = models.ForeignKey(BudgetName, on_delete=models.CASCADE, default=1)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, blank=True, default=1)
    prevision = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    spent = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name.name

    @property
    def over(self):
        return self.spent - min(self.spent, self.prevision)

    @property
    def theoretical_spending(self):
        current_progress = self.month.month_progress
        return Decimal(current_progress) * Decimal(self.prevision)

    @property
    def remaining_over(self):
        return max(self.theoretical_spending - self.spent, 0)

    @property
    def remaining_ok(self):
        return self.prevision - max(self.spent, self.theoretical_spending)

    @property
    def spent_ok(self):
        return min(self.spent, self.theoretical_spending)

    @property
    def spent_over(self):
        return max(self.spent - self.theoretical_spending, 0)

    @property
    def delta_days(self):
        return round((self.spent - self.theoretical_spending) / (self.month.nb_days + 1))

    def set_prevision_to(self, prevision):
        self.prevision = prevision


class Operation(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField('Date', default=datetime.date.today)
    budget = models.ForeignKey(BudgetName, on_delete=models.CASCADE, default=1)
    check = models.NullBooleanField(default=False)
    payment = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name + ' : '+str(self.amount)

    def is_recent_or_pending(self):
        now = datetime.date.today()
        if self.date > now - datetime.timedelta(days=self.payment.nb_days_operations_remain_visible):
            return True # RECENT
        return not self.check and not self.payment.instant_payment #PENDING
