# Generated by Django 2.0.4 on 2018-05-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0010_auto_20180507_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='Город'),
        ),
    ]
