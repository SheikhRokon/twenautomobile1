# Generated by Django 3.2.13 on 2022-06-26 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automobileapp', '0023_coursetype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_type',
        ),
    ]
