# Generated by Django 2.0.4 on 2018-05-17 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0059_auto_20180517_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='worldtravelapp.Tour', verbose_name='Тур'),
        ),
    ]