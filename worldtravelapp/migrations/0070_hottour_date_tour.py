# Generated by Django 2.0.4 on 2018-05-18 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0069_remove_hottour_date_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='hottour',
            name='date_tour',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата тура'),
        ),
    ]
