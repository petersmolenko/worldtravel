# Generated by Django 2.0.4 on 2018-05-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0021_auto_20180509_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearestdate',
            name='tours_list',
            field=models.ManyToManyField(blank=True, related_name='dates', to='worldtravelapp.Tour', verbose_name='Туры'),
        ),
    ]
