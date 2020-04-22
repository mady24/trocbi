# Generated by Django 3.0.4 on 2020-04-21 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20200421_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postprop',
            name='sous_famille',
        ),
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 21, 13, 48, 42, 637190, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 21, 13, 48, 42, 638210, tzinfo=utc)),
        ),
    ]
