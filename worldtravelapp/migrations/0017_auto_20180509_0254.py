# Generated by Django 2.0.4 on 2018-05-08 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0016_auto_20180509_0221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]