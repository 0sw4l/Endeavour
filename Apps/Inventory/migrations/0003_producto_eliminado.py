# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='eliminado',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
