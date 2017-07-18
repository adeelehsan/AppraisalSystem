# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Employee(models.Model):
    """
        An Employee class - to describe Employee in the system.
    """
    user = models.OneToOneField(User, unique=True)
    address = models.CharField(max_length=200)
    employee_type = models.CharField(max_length=200)
    report_to = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class Competencies(models.Model):
    skills = models.CharField(max_length=200)
    communication = models.CharField(max_length=200)


class Appraisal(models.Model):
    """
        An Appraisal class - to describe Appraisal in the system.
    """
    year = models.IntegerField()
    employee_score = models.IntegerField()
    manager_comment = models.CharField(max_length=300)
    competencies = models.ForeignKey(Competencies, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


