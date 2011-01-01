# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20151122_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='credito',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
