# Generated by Django 2.0.3 on 2018-05-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0015_auto_20180430_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='upcoming_balance',
            new_name='upcoming_delta',
        ),
        migrations.AlterField(
            model_name='operation',
            name='check',
            field=models.NullBooleanField(default=False),
        ),
    ]
