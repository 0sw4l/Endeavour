# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_remove_cliente_key_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cliente',
            field=models.BooleanField(default=True),
        ),
    ]
