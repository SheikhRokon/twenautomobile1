# Generated by Django 3.2.13 on 2022-06-11 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automobileapp', '0003_notice_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-id', 'ordering']},
        ),
    ]
