# Generated by Django 3.0.6 on 2020-06-05 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20200605_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
