# Generated by Django 3.0.4 on 2020-04-21 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20200421_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='sousfamille',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 21, 13, 15, 5, 478636, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 21, 13, 15, 5, 479635, tzinfo=utc)),
        ),
    ]