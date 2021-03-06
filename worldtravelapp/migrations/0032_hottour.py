# Generated by Django 2.0.4 on 2018-05-12 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0031_auto_20180512_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotTour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, upload_to='news_images/', verbose_name='Фото тура')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotturs', to='worldtravelapp.Tour', verbose_name='Тур')),
            ],
            options={
                'verbose_name': 'Горящий тур',
                'verbose_name_plural': 'Горящие туры',
            },
        ),
    ]
