# Generated by Django 2.0.4 on 2018-05-12 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0030_auto_20180512_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citys', to='worldtravelapp.Country', verbose_name='Страна'),
        ),
    ]
