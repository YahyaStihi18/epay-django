# Generated by Django 3.0.6 on 2020-06-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20200601_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]