# Generated by Django 3.1.2 on 2021-04-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]
