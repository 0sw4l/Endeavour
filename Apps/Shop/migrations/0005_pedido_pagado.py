# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_pedido_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
    ]
