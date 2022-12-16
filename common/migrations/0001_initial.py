# Generated by Django 4.1.3 on 2022-11-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=20)),
                ('Email_address', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('Phone_number', models.BigIntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('Cust_password', models.CharField(max_length=10)),
            ],
        ),
    ]
