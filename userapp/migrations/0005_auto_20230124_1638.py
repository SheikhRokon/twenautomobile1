# Generated by Django 3.2.13 on 2023-01-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_rename_regionname_userip_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='userip',
            name='status',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='userip',
            name='user_ip',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
