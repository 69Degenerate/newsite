# Generated by Django 3.1.1 on 2022-09-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_man_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]