# Generated by Django 2.0.4 on 2018-05-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0003_auto_20180503_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='news_images', verbose_name='Фото к статье'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_prev',
            field=models.ImageField(blank=True, default='', upload_to='news_images', verbose_name='Фото превью'),
        ),
    ]
