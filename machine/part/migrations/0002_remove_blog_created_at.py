# Generated by Django 4.0.3 on 2022-04-11 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
    ]
