from django.conf.urls import url
from . import views

app_name = 'EmployeeAppraisalapp'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'summary', views.summary, name='summary'),
    url(r'create', views.create_employee, name='create_employee'),
    url(r'feedback', views.create_appraisal, name='create_appraisal'),
    # url(r'^(?P<todo_id>[0-9]+)/delete', views.delete, name='delete'),
    # url(r'^(?P<todo_id>[0-9]+)/detail', views.detail, name='detail'),
    # url(r'^(?P<todo_id>[0-9]+)/update', views.update, name='update'),
    # url(r'update', views.update, name='update'),
]
