# Generated by Django 3.0.6 on 2020-06-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0069_service_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='model',
            field=models.CharField(choices=[('credit', 'credit'), ('game', 'game'), ('other', 'other')], max_length=20, null=True),
        ),
    ]
