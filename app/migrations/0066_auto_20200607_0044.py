# Generated by Django 3.0.6 on 2020-06-06 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20200607_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='saller',
        ),
        migrations.AddField(
            model_name='service',
            name='distributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Distributor'),
        ),
    ]
