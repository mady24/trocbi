# Generated by Django 3.0.4 on 2020-06-11 09:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20200515_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='postprop',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 11, 9, 1, 13, 772370, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 11, 9, 1, 13, 769955, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 11, 9, 1, 13, 770930, tzinfo=utc)),
        ),
    ]