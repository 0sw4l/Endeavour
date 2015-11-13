# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_tipoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(default=0, to='Inventory.TipoProducto'),
            preserve_default=False,
        ),
    ]
