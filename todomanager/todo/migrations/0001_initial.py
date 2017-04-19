# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='Description Chambre', max_length=60)),
                ('roomnumber', models.IntegerField(verbose_name='Numero Chambre')),
                ('etage', models.IntegerField(verbose_name='Etage')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('surname', models.CharField(verbose_name='Prénom', max_length=60)),
                ('phone', models.CharField(verbose_name='phone', max_length=60)),
                ('mail', models.CharField(verbose_name='mail', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotelname', models.CharField(verbose_name='Nomhotel', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DateDebut', models.DateField(verbose_name='Date Debut')),
                ('DateFin', models.DateField(verbose_name='Date Fin')),
                ('chambre', models.ForeignKey(verbose_name='chambre', to='todo.Chambre')),
                ('client', models.ForeignKey(verbose_name='client', to='todo.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('description', models.TextField(verbose_name='Description', blank=True, null=True)),
                ('due_date', models.DateTimeField(verbose_name='Fin prévue le', default=datetime.datetime(2017, 4, 20, 14, 17, 17, 216396, tzinfo=utc), blank=True, null=True)),
                ('completed', models.BooleanField(verbose_name='Tache terminée ? ', default=False)),
                ('status', models.CharField(default=None, max_length=20, blank=True, choices=[(None, '---')], null=True)),
            ],
        ),
    ]
