# Generated by Django 3.1.2 on 2021-05-12 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lmn', '0004_auto_20210505_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmn.show'),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='show',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmn.artist'),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='show',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmn.venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]