# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(),
            preserve_default=False,
        ),
    ]
