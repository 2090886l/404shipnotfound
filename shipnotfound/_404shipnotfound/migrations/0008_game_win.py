# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_404shipnotfound', '0007_auto_20150314_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='win',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
