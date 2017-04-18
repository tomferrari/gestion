# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=60, verbose_name='DescriptionChambre')),
                ('roomnumber', models.IntegerField(verbose_name='NumeroChambre')),
                ('etage', models.IntegerField(verbose_name='Etage')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('surname', models.CharField(max_length=60, verbose_name='Prénom')),
                ('phone', models.CharField(max_length=60, verbose_name='phone')),
                ('mail', models.CharField(max_length=60, verbose_name='mail')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=60, verbose_name='Nomhotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateDebut', models.DateTimeField(verbose_name='DateDebut')),
                ('DateFin', models.DateTimeField(verbose_name='DateFin')),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Chambre', verbose_name='Paramêtres')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Client', verbose_name='Paramêtres')),
            ],
        ),
    ]
