# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeAppraisalapp', '0002_employee_report_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='report_to',
        ),
    ]
