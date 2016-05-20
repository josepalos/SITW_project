# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0022_auto_20160520_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='user',
            new_name='owner',
        ),
    ]
