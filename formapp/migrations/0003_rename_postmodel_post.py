# Generated by Django 4.2.6 on 2024-01-22 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_alter_postmodel_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostModel',
            new_name='Post',
        ),
    ]
