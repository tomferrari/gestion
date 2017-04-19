# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20170419_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambre',
            name='description',
            field=models.TextField(max_length=60, verbose_name='Description Chambre'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='roomnumber',
            field=models.IntegerField(verbose_name='Numero Chambre'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateDebut',
            field=models.DateField(verbose_name='Date Debut'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateFin',
            field=models.DateField(verbose_name='Date Fin'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, default=datetime.datetime(2017, 4, 20, 13, 50, 3, 764462, tzinfo=utc), blank=True, verbose_name='Fin prévue le'),
        ),
    ]
