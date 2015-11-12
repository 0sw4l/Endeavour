# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_cliente_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cliente',
        ),
    ]
