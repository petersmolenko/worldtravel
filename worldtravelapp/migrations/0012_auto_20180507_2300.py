# Generated by Django 2.0.4 on 2018-05-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0011_auto_20180507_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, default='', verbose_name='День рождения'),
        ),
    ]
