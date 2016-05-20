# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0023_auto_20160520_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together=set([('name', 'owner')]),
        ),
    ]
