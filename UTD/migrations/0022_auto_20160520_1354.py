# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTD', '0021_auto_20160519_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together=set([('name', 'user')]),
        ),
    ]
