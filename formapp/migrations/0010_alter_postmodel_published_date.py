# Generated by Django 4.2.6 on 2024-01-31 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0009_alter_postmodel_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 31, 10, 36, 40, 244516), null=True),
        ),
    ]
