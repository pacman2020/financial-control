# Generated by Django 3.1.2 on 2020-11-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20201101_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='active',
            field=models.BooleanField(),
        ),
    ]