# Generated by Django 2.0.4 on 2018-05-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default='1970-01-01', verbose_name='День рождения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='Белгород', max_length=30, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='images/users', verbose_name='Фото профиля'),
        ),
    ]