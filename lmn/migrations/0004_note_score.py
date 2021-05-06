# Generated by Django 3.1.2 on 2021-05-03 02:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]