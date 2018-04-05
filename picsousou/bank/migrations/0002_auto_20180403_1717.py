# Generated by Django 2.0.3 on 2018-04-03 17:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bank.Person'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 4, 3, 17, 17, 25, 826514, tzinfo=utc), verbose_name='Date'),
        ),
    ]