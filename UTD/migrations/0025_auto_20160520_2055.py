# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0024_auto_20160520_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together=set([('name', 'user')]),
        ),
    ]
