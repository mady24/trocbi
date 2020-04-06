# Generated by Django 3.0.4 on 2020-03-18 02:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200318_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='postprop',
            name='name',
            field=models.CharField(default='firstcommit', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 18, 2, 12, 52, 289279, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 3, 18, 2, 12, 52, 290358, tzinfo=utc)),
        ),
    ]
