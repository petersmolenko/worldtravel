# Generated by Django 2.0.4 on 2018-05-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0050_auto_20180515_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер телефона'),
        ),
    ]