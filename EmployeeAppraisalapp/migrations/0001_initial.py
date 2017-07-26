# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 04:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('employee_score', models.IntegerField()),
                ('manager_comment', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Competencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=200)),
                ('communication', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('employee_type', models.CharField(max_length=200)),
                ('report_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EmployeeAppraisalapp.Employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appraisal',
            name='competencies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeAppraisalapp.Competencies'),
        ),
        migrations.AddField(
            model_name='appraisal',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeAppraisalapp.Employee'),
        ),
    ]
