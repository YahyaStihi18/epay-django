# Generated by Django 3.0.6 on 2020-05-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200530_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.FileField(default='defser.png', upload_to='app/recu'),
        ),
    ]