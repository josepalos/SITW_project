# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.TextField(default='unknown'),
            preserve_default=False,
        ),
    ]
