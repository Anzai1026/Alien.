# Generated by Django 4.2.6 on 2024-01-31 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0012_alter_postmodel_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 31, 11, 17, 34, 825950), null=True),
        ),
    ]
