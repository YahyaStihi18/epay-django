# Generated by Django 3.0.6 on 2020-06-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0068_auto_20200607_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
