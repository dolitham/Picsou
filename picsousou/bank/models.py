from django.db import models
import datetime


class Month(models.Model):
    first_day = models.DateField('First Day')
    last_day = models.DateField('Last Day')
    total_input = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total_output = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    @property
    def nb_days(self):
        days = self.last_day-self.first_day
        return days.days+1

    @property
    def id_name(self):
        middle_date = self.first_day + datetime.timedelta(days=self.nb_days//2)
        return middle_date.strftime("%b %Y")

    def __str__(self):
        return str(self.id_name)


class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=50)
    id_name = models.CharField(max_length=10)
    current_balance = models.DecimalField(max_digits=7, decimal_places=2)
    upcoming_balance = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    visible_days = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' ' + self.account.id_name


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
    def first_day(self):
        return self.month.first_day

    @property
    def last_day(self):
        return self.month.last_day

    def set_prev_to(self, prevision):
        self.prevision = prevision


class Operation(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField('Date', default=datetime.date.today)
    budget = models.ForeignKey(BudgetName, on_delete=models.CASCADE, default=1)
    check = models.BooleanField(default=False)
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name + ' : '+str(self.amount)

    @property
    def account(self):
        return self.payment.account

    def is_recent_or_pending(self):
        is_pending = not self.check and self.payment.visible_days == 0
        if is_pending:
            return True
        now = datetime.date.today()
        is_recent = self.date > now - datetime.timedelta(days=self.payment.visible_days)
        print(self.name, is_recent)
        return is_recent
