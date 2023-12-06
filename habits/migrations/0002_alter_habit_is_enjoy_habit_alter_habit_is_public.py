# Generated by Django 4.2.7 on 2023-12-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='is_enjoy_habit',
            field=models.BooleanField(default=False, verbose_name='признак приятной привычки'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='признак публичной привычки'),
        ),
    ]
