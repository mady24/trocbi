# Generated by Django 3.0.4 on 2020-04-05 09:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200405_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 5, 9, 38, 16, 873301, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 5, 9, 38, 16, 874334, tzinfo=utc)),
        ),
    ]
