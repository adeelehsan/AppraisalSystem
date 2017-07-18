# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import EmployeeForm, AppraisalForm

# Create your views here.


def create_employee(request):
    if request.POST:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('EmployeeAppraisalapp:index'))
        else:
            return render(request, 'EmployeeAppraisalapp/create.html', {'form': form})
    else:
        return render(request, 'EmployeeAppraisalapp/create.html', {'form': EmployeeForm()})


def create_appraisal(request):
    if request.POST:
        form = AppraisalForm(request.POST)
        if form.is_valid():
            Appraisal = form.save(commit=False)
            Appraisal.employee = request.user
            form.save()
            return HttpResponseRedirect(reverse('EmployeeAppraisalapp:index'))
        else:
            return render(request, 'EmployeeAppraisalapp/create.html', {'form': form})
    else:
        return render(request, 'EmployeeAppraisalapp/create.html', {'form': AppraisalForm()})