# Generated by Django 4.0.3 on 2022-06-10 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentMan', '0003_alter_customuser_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classofschool',
            name='classId',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dateOfBirth',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 0, 0)),
        ),
    ]
