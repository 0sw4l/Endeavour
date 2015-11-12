# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20151111_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='key_expires',
        ),
    ]
