# Generated by Django 3.0.4 on 2020-04-05 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200401_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='postprop',
            name='typeProp',
            field=models.CharField(choices=[('offre', 'offre'), ('demande', 'demande')], default='offre', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postsearch',
            name='name',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 5, 9, 30, 30, 883962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 5, 9, 30, 30, 884936, tzinfo=utc)),
        ),
    ]
