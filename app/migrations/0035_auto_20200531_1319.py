# Generated by Django 3.0.6 on 2020-05-31 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20200531_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='facebook',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='servicegame',
            name='currency',
            field=models.CharField(choices=[('€', '€'), ('$', '$'), ('DZD', 'DZD'), ('Unit', 'Unit')], max_length=20, null=True),
        ),
    ]