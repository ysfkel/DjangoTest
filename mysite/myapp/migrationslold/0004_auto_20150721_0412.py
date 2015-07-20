# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150721_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name_text',
            field=models.CharField(max_length=50),
        ),
    ]
