# Generated by Django 3.2.13 on 2023-01-24 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20230124_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userip',
            name='status',
        ),
    ]
