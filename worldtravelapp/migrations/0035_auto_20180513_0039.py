# Generated by Django 2.0.4 on 2018-05-12 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0034_hottour_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='discount_tour',
            field=models.BooleanField(default=False, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='hottour',
            name='tour',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hottur', to='worldtravelapp.Tour', verbose_name='Тур'),
        ),
    ]
