# -*- coding: utf-8 -*-
<<<<<<< HEAD
from __future__ import unicode_literals

from django.db import migrations, models
=======
# Generated by Django 1.11 on 2017-04-18 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e


class Migration(migrations.Migration):

<<<<<<< HEAD
=======
    initial = True

>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(verbose_name='DescriptionChambre', max_length=60)),
                ('roomnumber', models.IntegerField(verbose_name='NumeroChambre', max_length=60)),
                ('etage', models.IntegerField(verbose_name='Etage', max_length=60)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=60, verbose_name='DescriptionChambre')),
                ('roomnumber', models.IntegerField(verbose_name='NumeroChambre')),
                ('etage', models.IntegerField(verbose_name='Etage')),
>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('surname', models.CharField(verbose_name='Prénom', max_length=60)),
                ('phone', models.CharField(verbose_name='phone', max_length=60)),
                ('mail', models.CharField(verbose_name='mail', max_length=60)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('surname', models.CharField(max_length=60, verbose_name='Prénom')),
                ('phone', models.CharField(max_length=60, verbose_name='phone')),
                ('mail', models.CharField(max_length=60, verbose_name='mail')),
>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('hotelname', models.CharField(verbose_name='Nomhotel', max_length=60)),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=60, verbose_name='Nomhotel')),
>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('DateDebut', models.IntegerField(verbose_name='DateDebut', max_length=60)),
                ('DateFin', models.IntegerField(verbose_name='DateFin', max_length=60)),
                ('chambre', models.ForeignKey(verbose_name='Paramêtres', to='todo.Chambre')),
                ('client', models.ForeignKey(verbose_name='Paramêtres', to='todo.Client')),
=======
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateDebut', models.DateTimeField(verbose_name='DateDebut')),
                ('DateFin', models.DateTimeField(verbose_name='DateFin')),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Chambre', verbose_name='Paramêtres')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Client', verbose_name='Paramêtres')),
>>>>>>> c97636a583ce97ffe82635943f6e7de3e6882b5e
            ],
        ),
    ]
