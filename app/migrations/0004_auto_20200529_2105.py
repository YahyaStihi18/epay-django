# Generated by Django 3.0.6 on 2020-05-29 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='latName',
            new_name='lastName',
        ),
    ]
