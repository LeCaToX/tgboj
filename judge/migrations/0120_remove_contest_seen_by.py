# Generated by Django 2.2.23 on 2021-05-25 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0119_auto_20210523_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='seen_by',
        ),
    ]
