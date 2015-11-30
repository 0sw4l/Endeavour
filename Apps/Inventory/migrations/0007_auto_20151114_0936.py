# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_remove_cliente_cliente'),
        ('Inventory', '0006_producto_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.TextField()),
                ('cliente', models.ForeignKey(to='Users.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='voto_negativo',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='voto_positivo',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to=b'endeavour'),
        ),
        migrations.AddField(
            model_name='comentarioproducto',
            name='producto',
            field=models.ForeignKey(to='Inventory.Producto'),
        ),
    ]
