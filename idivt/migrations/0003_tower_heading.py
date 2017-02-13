# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idivt', '0002_line_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='heading',
            field=models.DecimalField(default=0, max_digits=20, decimal_places=15),
            preserve_default=False,
        ),
    ]
