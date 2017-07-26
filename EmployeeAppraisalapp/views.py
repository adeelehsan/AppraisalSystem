# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from .forms import EmployeeForm, AppraisalForm
from django.contrib.auth.models import User
from .models import Employee, Competencies, Appraisal


# Create your views here.
@login_required
def index(request):
    employee = Employee.objects.get(user=request.user)
    if employee.employee_type == 'CEO' or employee.employee_type == 'Manager':
        empolyee_list = Employee.objects.filter(report_to=employee)
        context = {'empolyee_list': empolyee_list, 'msg': 'manager'}
    else:
        feedback = Appraisal.objects.filter(employee=employee)
        context = {'feedback': feedback, 'msg': 'employee'}
    return render(request, 'EmployeeAppraisalapp/index.html', context)


@login_required
def create_employee(request):
    if request.POST:
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'])
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = user
            form.save()
            return render(request, 'EmployeeAppraisalapp/create.html', {'form': form})
        else:
            return render(request, 'EmployeeAppraisalapp/create.html', {'form': form})
    else:
        return render(request, 'EmployeeAppraisalapp/create.html', {'form': EmployeeForm()})


@login_required
def create_appraisal(request):
    if request.POST:
        form = AppraisalForm(request.POST)
        if form.is_valid():
            competencies = Competencies.objects.create(skills=request.POST['skills'],
                                                       communication=request.POST['communications'])
            appraisal = form.save(commit=False)
            appraisal.competencies = competencies
            form.save()
            employee = Employee.objects.get(user=request.user)
            repot_to = employee.report_to
            send_mail(
                'Subject here',
                'Here is the message.',
                'adeel.ehsan@outlook.com',
                ['adeel.ehsan@arbisoft.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('EmployeeAppraisalapp:index'))
        else:
            return render(request, 'EmployeeAppraisalapp/feedback.html', {'form': form})
    else:
        return render(request, 'EmployeeAppraisalapp/feedback.html', {'form': AppraisalForm()})
