# Generated by Django 3.2.7 on 2023-04-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolled', '0022_remove_bkashpayment_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkashpayment',
            name='course',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
