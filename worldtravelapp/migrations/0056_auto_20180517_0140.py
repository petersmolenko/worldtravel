# Generated by Django 2.0.4 on 2018-05-16 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0055_auto_20180517_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearestdate',
            name='tour',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='nearestdates', to='worldtravelapp.Tour', verbose_name='Тур'),
        ),
    ]