# Generated by Django 3.0.6 on 2020-05-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200529_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('latName', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
