# Generated by Django 3.2.7 on 2023-04-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolled', '0016_bkashpayment_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='bkashpayment',
            name='title',
            field=models.CharField(default='hello', max_length=400),
        ),
        migrations.AddField(
            model_name='order',
            name='order_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]