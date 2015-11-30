# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0008_auto_20151122_2044'),
        ('Shop', '0002_pedido_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidodetalle',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cantidad',
            field=models.PositiveIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(to='Inventory.Producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.PositiveIntegerField(),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PedidoDetalle',
        ),
    ]
