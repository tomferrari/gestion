# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(verbose_name='DescriptionChambre', max_length=60)),
                ('roomnumber', models.IntegerField(verbose_name='NumeroChambre', max_length=60)),
                ('etage', models.IntegerField(verbose_name='Etage', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('surname', models.CharField(verbose_name='Prénom', max_length=60)),
                ('phone', models.CharField(verbose_name='phone', max_length=60)),
                ('mail', models.CharField(verbose_name='mail', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('hotelname', models.CharField(verbose_name='Nomhotel', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('DateDebut', models.IntegerField(verbose_name='DateDebut', max_length=60)),
                ('DateFin', models.IntegerField(verbose_name='DateFin', max_length=60)),
                ('chambre', models.ForeignKey(verbose_name='Paramêtres', to='todo.Chambre')),
                ('client', models.ForeignKey(verbose_name='Paramêtres', to='todo.Client')),
            ],
        ),
    ]
