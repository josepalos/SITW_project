# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0013_auto_20160417_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='last_update',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
