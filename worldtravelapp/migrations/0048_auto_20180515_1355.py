# Generated by Django 2.0.4 on 2018-05-15 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldtravelapp', '0047_auto_20180515_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='approved_reviews',
            new_name='approved_review',
        ),
    ]