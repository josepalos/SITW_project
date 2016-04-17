# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0015_auto_20160417_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='last_update',
            new_name='update_time',
        ),
    ]
