# Generated by Django 3.2.7 on 2023-06-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Student_data',
                'verbose_name_plural': 'Student_datas',
            },
        ),
    ]