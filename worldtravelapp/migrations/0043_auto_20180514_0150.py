# Generated by Django 2.0.4 on 2018-05-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0042_auto_20180514_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearestdate',
            name='count_place',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество мест'),
        ),
    ]