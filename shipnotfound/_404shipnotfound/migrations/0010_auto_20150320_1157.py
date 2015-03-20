# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_404shipnotfound', '0009_auto_20150320_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=b"{% static 'brightkite.png' %}", upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
    ]
