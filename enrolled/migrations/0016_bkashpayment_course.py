# Generated by Django 3.2.7 on 2023-04-04 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobileapp', '0043_alter_course_course_type'),
        ('enrolled', '0015_delete_bookinstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='bkashpayment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='automobileapp.course'),
        ),
    ]
