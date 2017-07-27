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
    report_to = models.ForeignKey('Employee', null=True)

    # def children(self, include_self=True):
    #     employee = []
    #     for employee in Employee.objects.filter(report_to=self.pk):
    #         _employee = employee.children(include_self=True)
    #         employee.append(_employee)
    #     return employee
    def get_all_children(self, include_self=True):
        r = []
        if include_self:
            r.append(self)
        for c in Employee.objects.filter(report_to=self):
            _r = c.get_all_children(include_self=True)
            if len(_r) > 0:
                r.extend(_r)
        return r

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


