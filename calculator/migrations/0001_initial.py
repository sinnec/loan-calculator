# Generated by Django 3.1.13 on 2021-08-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=25)),
                ('available_plans', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('months', models.PositiveIntegerField()),
            ],
        ),
    ]