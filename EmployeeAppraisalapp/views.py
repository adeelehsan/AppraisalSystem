# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def create_employee(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            return render(request, 'todo/create.html', {'form': form})
    else:
        return render(request, 'todo/create.html', {'form': TaskForm()})