# Generated by Django 3.2.5 on 2021-08-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=300)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female')], null=True)),
            ],
        ),
    ]
