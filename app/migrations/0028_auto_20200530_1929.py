# Generated by Django 3.0.6 on 2020-05-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20200530_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
