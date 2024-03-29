# Generated by Django 3.0.4 on 2020-03-18 02:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postprop',
            name='durée_util',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postprop',
            name='prix_achat',
            field=models.FloatField(default=100000, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(default='2020-03-18', verbose_name=datetime.datetime(2020, 3, 18, 2, 3, 45, 326372, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postsearch',
            name='durée_util',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(default='2020-03-18', verbose_name=datetime.datetime(2020, 3, 18, 2, 3, 45, 327064, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
