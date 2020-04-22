# Generated by Django 3.0.4 on 2020-04-21 12:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20200414_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='naturebien',
            name='famille',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.SousFamille'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='postprop',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 21, 12, 28, 8, 692147, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postsearch',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 21, 12, 28, 8, 693113, tzinfo=utc)),
        ),
    ]
