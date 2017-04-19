# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20170418_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('description', models.TextField(verbose_name='Description', blank=True, null=True)),
                ('due_date', models.DateTimeField(verbose_name='Fin prévue le', default=datetime.datetime(2017, 4, 20, 13, 15, 22, 588111, tzinfo=utc), blank=True, null=True)),
                ('completed', models.BooleanField(verbose_name='Tache terminée ? ', default=False)),
                ('status', models.CharField(default=None, max_length=20, choices=[(None, '---')], blank=True, null=True)),
            ],
        ),
    ]
