# Generated by Django 3.0.6 on 2020-05-30 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200530_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='accountId',
            new_name='accountIds',
        ),
    ]
