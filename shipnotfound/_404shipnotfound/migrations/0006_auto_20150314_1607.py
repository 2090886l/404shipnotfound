# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_404shipnotfound', '0005_auto_20150314_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
