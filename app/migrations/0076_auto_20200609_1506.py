# Generated by Django 3.0.6 on 2020-06-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0075_auto_20200609_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
