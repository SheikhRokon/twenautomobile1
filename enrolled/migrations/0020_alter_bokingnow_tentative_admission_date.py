# Generated by Django 3.2.7 on 2023-04-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolled', '0019_auto_20230406_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokingnow',
            name='tentative_admission_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]