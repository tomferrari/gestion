# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20170419_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='DateFin',
            field=models.DateField(verbose_name='DateFin'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='Fin prévue le', null=True, default=datetime.datetime(2017, 4, 20, 13, 27, 33, 9742, tzinfo=utc), blank=True),
        ),
    ]
