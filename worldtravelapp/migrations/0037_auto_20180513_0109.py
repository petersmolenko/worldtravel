# Generated by Django 2.0.4 on 2018-05-12 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0036_auto_20180513_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hottour',
            name='tour',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hottour', to='worldtravelapp.Tour', verbose_name='Тур'),
        ),
    ]
