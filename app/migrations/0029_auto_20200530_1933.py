# Generated by Django 3.0.6 on 2020-05-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20200530_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='distributor',
        ),
        migrations.AddField(
            model_name='order',
            name='saller',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]