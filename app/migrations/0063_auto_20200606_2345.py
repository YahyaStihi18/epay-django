# Generated by Django 3.0.6 on 2020-06-06 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_service_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
    ]
