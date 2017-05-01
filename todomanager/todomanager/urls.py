"""todomanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


#from todo.views import TaskListView, TaskCreateView, TaskRetrieveView, TaskUpdateView, TaskDeleteView





from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo.views import LoginView, LogoutView
from rest_framework import routers
#from eboutique.views import *
#from erp.views import *
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', TaskListView.as_view(), name='task-list'),
    # url(r'^create/$', TaskCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/$', TaskRetrieveView.as_view(), name='retrieve'),
    # url(r'^(?P<pk>\d+)/update/$', TaskUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='delete'),
]

    url(r'^$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^backoffice/$', login_required(TemplateView.as_view(template_name='backoffice/index.html'))),
)

