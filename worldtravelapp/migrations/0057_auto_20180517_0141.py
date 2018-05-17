# Generated by Django 2.0.4 on 2018-05-16 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0056_auto_20180517_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearestdate',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nearestdates', to='worldtravelapp.Tour', verbose_name='Тур'),
        ),
        migrations.AlterUniqueTogether(
            name='nearestdate',
            unique_together={('tour', 'date')},
        ),
    ]
