# Generated by Django 3.1.7 on 2021-03-11 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evraka', '0003_auto_20210311_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationrecord',
            name='plate',
            field=models.CharField(max_length=50, null=True, verbose_name='Araç Plakası'),
        ),
        migrations.AlterField(
            model_name='navigationrecord',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
