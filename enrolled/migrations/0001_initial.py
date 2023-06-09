# Generated by Django 3.2.13 on 2022-07-24 05:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('automobileapp', '0036_alter_blog_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobileapp.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_to', models.DateTimeField(default=django.utils.timezone.now)),
                ('max_value', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Coupon Quantity')),
                ('used', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField()),
                ('order_complate_date', models.DateTimeField(blank=True, null=True)),
                ('order_status', models.CharField(choices=[('pending', 'pending'), ('processing', 'processing'), ('unpaid', 'unpaid'), ('paid', 'paid')], default='pending', max_length=150)),
                ('total_order_amount', models.CharField(blank=True, max_length=150, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('orderId', models.CharField(blank=True, max_length=150, null=True)),
                ('paymentId', models.CharField(blank=True, max_length=150, null=True)),
                ('payment_option', models.CharField(max_length=150)),
                ('cart_items', models.ManyToManyField(to='enrolled.CartItem')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='enrolled.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
