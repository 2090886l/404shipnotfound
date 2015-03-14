# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_404shipnotfound', '0002_auto_20150314_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
