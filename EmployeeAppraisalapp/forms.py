from django import forms
from .models import Employee
from django.contrib import admin


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password', 'address']

    def clean(self):
        if not self.cleaned_data.get('username') or not self.cleaned_data.get('password'):
            raise forms.ValidationError(
                "Please Fill all the fields")


class TaskAdmin(admin.ModelAdmin):
    form = EmployeeForm
