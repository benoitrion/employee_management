# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=12)),
                ('mail', models.EmailField(max_length=254)),
                ('working_place', models.CharField(max_length=50)),
                ('working_contract', models.CharField(max_length=8, choices=[(b'CDD', b'CDD'), (b'CDI', b'CDI'), (b'CDD_CDI', b'CDD-CDI'), (b'INTERIM', b'Interim'), (b'REP', b'Replacement'), (b'ALE', b'ALE'), (b'UNDEFINED', b'Undefined')])),
                ('working_schedule', models.CharField(max_length=8, choices=[(b'CDD', b'CDD'), (b'CDI', b'CDI'), (b'CDD_CDI', b'CDD-CDI'), (b'INTERIM', b'Interim'), (b'REP', b'Replacement'), (b'ALE', b'ALE'), (b'UNDEFINED', b'Undefined')])),
                ('working_task', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateTimeField(verbose_name=b'date from')),
                ('date_to', models.DateTimeField(verbose_name=b'date to')),
                ('absence_reason', models.CharField(max_length=200, verbose_name=b'absence reason')),
                ('emp_abs', models.ForeignKey(related_name='emp_abs', verbose_name=b'absent employee', to='employees_management.Employee')),
                ('emp_rep', models.ForeignKey(related_name='emp_rep', verbose_name=b'replacement employee', to='employees_management.Employee')),
            ],
        ),
    ]
