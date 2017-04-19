# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170418_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='chambre',
            field=models.ForeignKey(verbose_name='chambre', to='todo.Chambre'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(verbose_name='client', to='todo.Client'),
        ),
    ]
