# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_remove_cliente_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='activation_key',
            new_name='token',
        ),
    ]
