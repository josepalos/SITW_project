# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0012_auto_20160417_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2016, 4, 17, 12, 46, 51, 864268, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(to='UTD.Song', blank=True),
        ),
    ]
