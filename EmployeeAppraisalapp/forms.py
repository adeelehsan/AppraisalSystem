from django import forms
from .models import Employee, Appraisal, User
from django.contrib import admin


class EmployeeForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # report_to = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['report_to'].required = False

    class Meta:
        model = Employee
        fields = ['username', 'password', 'address', 'employee_type', 'report_to']

    def clean(self):
        if not self.cleaned_data.get('username'):
            raise forms.ValidationError(
                "Please Fill all the fields")


class AppraisalForm(forms.ModelForm):
    skills = forms.CharField()
    communications = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Appraisal
        fields = '__all__'
        exclude = ['employee', 'competencies']

    def clean(self):
        if not self.cleaned_data.get('user'):
            raise forms.ValidationError(
                "Please Fill all the fields")


class TaskAdmin(admin.ModelAdmin):
    form = EmployeeForm
