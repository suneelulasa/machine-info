# Generated by Django 4.0.4 on 2022-04-14 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0008_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 15, 31, 6, 994411)),
        ),
    ]
