# Generated by Django 3.0.6 on 2020-05-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20200530_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(default='nothing.png', upload_to=''),
        ),
    ]
