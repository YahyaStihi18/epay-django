# Generated by Django 3.0.6 on 2020-05-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200530_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='accountId',
            field=models.TextField(default=''),
        ),
    ]
