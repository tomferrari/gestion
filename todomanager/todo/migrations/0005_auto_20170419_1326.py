# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='DateDebut',
            field=models.DateTimeField(verbose_name='DateDebut'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateFin',
            field=models.DateTimeField(verbose_name='DateFin'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(verbose_name='Fin prévue le', default=datetime.datetime(2017, 4, 20, 13, 26, 48, 972329, tzinfo=utc), null=True, blank=True),
        ),
    ]
