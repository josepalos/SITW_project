# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0005_auto_20160416_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userartistslist',
            name='followed_artist',
        ),
        migrations.AddField(
            model_name='userartistslist',
            name='followed_artist',
            field=models.ManyToManyField(to='UTD.Artist'),
        ),
    ]
