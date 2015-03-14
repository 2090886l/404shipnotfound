# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_404shipnotfound', '0003_auto_20150314_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
