# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0019_auto_20160509_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='spotify_id',
            field=models.TextField(default='...'),
            preserve_default=False,
        ),
    ]
