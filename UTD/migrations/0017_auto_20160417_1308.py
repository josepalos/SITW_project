# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0016_auto_20160417_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='update_time',
            new_name='last_update',
        ),
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.TextField(default=b'Following'),
        ),
    ]
