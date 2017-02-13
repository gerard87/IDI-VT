# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idivt', '0003_tower_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tower',
            name='heading',
        ),
    ]
