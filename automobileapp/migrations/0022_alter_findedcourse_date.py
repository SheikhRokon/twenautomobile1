# Generated by Django 3.2.13 on 2022-06-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobileapp', '0021_findedcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findedcourse',
            name='date',
            field=models.DateField(),
        ),
    ]
