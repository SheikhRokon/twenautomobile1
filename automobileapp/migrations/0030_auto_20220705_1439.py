# Generated by Django 3.2.13 on 2022-07-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automobileapp', '0029_auto_20220701_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='upcommingcourse',
            name='course_discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
