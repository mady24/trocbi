# Generated by Django 3.0.4 on 2020-04-14 09:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20200414_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 14, 9, 18, 52, 145525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 14, 9, 18, 52, 146590, tzinfo=utc)),
        ),
    ]
