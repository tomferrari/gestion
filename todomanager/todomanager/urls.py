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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#from todo.views import TaskListView, TaskCreateView, TaskRetrieveView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
    url(r'^$', TemplateView.as_view(template_name="todo/base.html"), name='todo'),


    # url(r'^$', TaskListView.as_view(), name='task-list'),
    # url(r'^create/$', TaskCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/$', TaskRetrieveView.as_view(), name='retrieve'),
    # url(r'^(?P<pk>\d+)/update/$', TaskUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', TaskDeleteView.as_view(), name='delete'),
]

