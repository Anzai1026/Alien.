# Generated by Django 4.2.6 on 2024-01-26 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0007_alter_postmodel_image_alter_postmodel_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 26, 14, 45, 18, 56751), null=True),
        ),
    ]
