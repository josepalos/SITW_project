# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0002_album_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.TextField(default=b'Unknown'),
        ),
    ]
