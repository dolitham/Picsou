# Generated by Django 2.0.3 on 2018-04-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_auto_20180406_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='visible_days',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
