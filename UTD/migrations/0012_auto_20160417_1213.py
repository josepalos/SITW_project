# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0011_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userartistslist',
            name='followed_artist',
        ),
        migrations.RemoveField(
            model_name='userartistslist',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserArtistsList',
        ),
    ]
