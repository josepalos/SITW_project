# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0017_auto_20160417_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='song',
            new_name='songs',
        ),
    ]
