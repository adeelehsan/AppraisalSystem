# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeAppraisalapp', '0003_remove_employee_report_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='report_to',
            field=models.CharField(max_length=200, null=True),
        ),
    ]