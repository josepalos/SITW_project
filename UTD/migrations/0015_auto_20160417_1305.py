# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0014_auto_20160417_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.TextField(default=b'Following playlist'),
        ),
    ]
