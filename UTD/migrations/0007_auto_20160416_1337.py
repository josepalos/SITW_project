# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0006_auto_20160416_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='related',
            field=models.ManyToManyField(related_name='_artist_related_+', to='UTD.Artist', blank=True),
        ),
        migrations.AlterField(
            model_name='userartistslist',
            name='followed_artist',
            field=models.ManyToManyField(to='UTD.Artist', blank=True),
        ),
    ]
