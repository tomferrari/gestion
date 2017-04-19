# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambre',
            name='etage',
            field=models.IntegerField(verbose_name='Etage'),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='roomnumber',
            field=models.IntegerField(verbose_name='NumeroChambre'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateDebut',
            field=models.IntegerField(verbose_name='DateDebut'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateFin',
            field=models.IntegerField(verbose_name='DateFin'),
        ),
    ]
