# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UTD', '0018_auto_20160417_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='provider',
            name='link',
            field=models.URLField(),
        ),
    ]
