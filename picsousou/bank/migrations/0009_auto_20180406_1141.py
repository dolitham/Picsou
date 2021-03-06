# Generated by Django 2.0.3 on 2018-04-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_auto_20180405_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='balance',
            new_name='current_balance',
        ),
        migrations.AddField(
            model_name='account',
            name='upcoming_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
    ]
