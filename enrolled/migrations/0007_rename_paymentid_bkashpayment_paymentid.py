# Generated by Django 3.2.13 on 2023-01-30 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrolled', '0006_bkashpayment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bkashpayment',
            old_name='PaymentId',
            new_name='paymentId',
        ),
    ]
