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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField(max_length=60, verbose_name='Description Chambre')),
                ('roomnumber', models.IntegerField(verbose_name='Numero Chambre')),
                ('etage', models.IntegerField(verbose_name='Etage')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('surname', models.CharField(max_length=60, verbose_name='Prénom')),
                ('phone', models.CharField(max_length=60, verbose_name='phone')),
                ('mail', models.CharField(max_length=60, verbose_name='mail')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hotelname', models.CharField(max_length=60, verbose_name='Nomhotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('DateDebut', models.DateField(verbose_name='Date Debut')),
                ('DateFin', models.DateField(verbose_name='Date Fin')),
                ('chambre', models.ForeignKey(to='todo.Chambre', verbose_name='chambre')),
                ('client', models.ForeignKey(to='todo.Client', verbose_name='client')),
            ],
        ),
    ]
