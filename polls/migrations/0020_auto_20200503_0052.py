# Generated by Django 3.0.4 on 2020-05-03 00:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20200502_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 5, 3, 0, 52, 56, 867342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 5, 3, 0, 52, 56, 868307, tzinfo=utc)),
        ),
    ]
