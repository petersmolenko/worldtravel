# Generated by Django 2.0.4 on 2018-05-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0062_tour_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[('AFR', 'Африка'), ('ASI', 'Азия'), ('AUS', 'Австралия'), ('RUS', 'Россия'), ('EUR', 'Европа'), ('SAM', 'Северная Америка'), ('NAM', 'Южная Америка')], default='RUS', max_length=3, verbose_name='Континент'),
        ),
    ]
