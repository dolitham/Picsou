from .database_manager import *


def date_str(date):
    return date.strftime('%d %b %Y')


def get_previous_and_next_month(month):
    months = Month.objects.order_by('first_day')
    nb_months = len(months)
    index_month = months.index(month)
    next_month = None if index_month == nb_months - 1 else months[index_month+1]
    prev_month = None if index_month == 0 else months[index_month - 1]
    return prev_month, next_month


def month_overlaps(month1, month2):
    delta1 = (month1.first_day - month2.last_day).days
    delta2 = (month1.last_day - month2.first_day).days
    return delta1*delta2 <= 0


def month_has_no_overlap(month):
    overlap = [m.id_name + '  (' + date_str(m.first_day) + ' to ' + date_str(m.last_day) + ')'for m in Month.objects.all() if month_overlaps(m, month)]
    return (True, []) if not overlap else (False, overlap)


def delete_month(month):
    operations = Operation.objects.filter(date__lte=month.last_day, date__gte=month.first_day)
    if operations:
        return False, len(operations)
    DataBaseManager.delete_month(month)
    return True, 0


def create_month(month):
    no_overlap, overlap_months = month_has_no_overlap(month)
    if no_overlap:
        month.save()
        return True, ''
    else:
        return False, overlap_months


def month_progress(month):
    today = datetime.date.today()
    if today > month.last_day:
        return 1
    if today < month.first_day:
        return 0
    days_spent = today - month.first_day + 1
    days_spent = days_spent.days
    return days_spent / month.nb_days
