# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import EmployeeForm, AppraisalForm
from .models import User


# Create your views here.


def create_employee(request):
    if request.POST:
        user = User.objects.create(username=request.POST['username'],
                                   password=request.POST['password'])
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = user
            form.save()
            return render(request, 'EmployeeAppraisalapp/create.html', {'form': 'User is Created Successfully'})
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
