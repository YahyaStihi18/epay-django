# Generated by Django 3.0.6 on 2020-06-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20200605_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='visible_for_buyer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='visible_for_saller',
            field=models.BooleanField(default=True),
        ),
    ]
