# Generated by Django 3.0.6 on 2020-05-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200530_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.FileField(upload_to='static/app/recu'),
        ),
    ]
