# Generated by Django 3.2.7 on 2023-04-08 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolled', '0024_auto_20230408_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(to='enrolled.CartItem'),
        ),
    ]
