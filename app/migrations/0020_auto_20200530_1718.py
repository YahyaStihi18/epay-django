# Generated by Django 3.0.6 on 2020-05-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200530_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(default='defser.png', upload_to=''),
        ),
    ]
