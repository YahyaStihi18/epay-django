# Generated by Django 3.0.6 on 2020-05-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200530_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='accountId',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='distributor',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
