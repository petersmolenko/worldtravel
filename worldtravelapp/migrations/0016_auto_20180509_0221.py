# Generated by Django 2.0.4 on 2018-05-08 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0015_auto_20180508_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date'], 'permissions': (('view_news', 'Просмотр поста'), ('change_news', 'Изменение поста'), ('delete_news', 'Удаление поста')), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]