# Generated by Django 3.0.6 on 2020-06-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_auto_20200609_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
