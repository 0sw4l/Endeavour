# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='key_expires',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
