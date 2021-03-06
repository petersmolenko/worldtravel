# Generated by Django 2.0.4 on 2018-05-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0060_auto_20180517_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='hottour',
            name='advertise',
            field=models.BooleanField(default=False, verbose_name='Реклама'),
        ),
        migrations.AddField(
            model_name='hottour',
            name='banner',
            field=models.ImageField(default='', upload_to='hottours_images/banners/', verbose_name='Баннер тура'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='photo',
            field=models.ImageField(blank=True, upload_to='citys_images/', verbose_name='Фото города'),
        ),
        migrations.AlterField(
            model_name='country',
            name='photo',
            field=models.ImageField(blank=True, upload_to='countrys_images/', verbose_name='Фото страны'),
        ),
        migrations.AlterField(
            model_name='hottour',
            name='photo',
            field=models.ImageField(upload_to='hottours_images/photos/', verbose_name='Фото тура'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='order_count',
            field=models.IntegerField(default=0, verbose_name='Количество заказов'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='tours_images/', verbose_name='Фото тура'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='workers_images/', verbose_name='Фото сотрудника'),
        ),
    ]
