# Generated by Django 4.0.3 on 2022-04-13 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0007_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 13, 11, 10, 8, 303704)),
        ),
    ]
