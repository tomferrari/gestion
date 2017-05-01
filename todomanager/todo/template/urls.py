# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="todo/base.html"), name='todo'),
    url(r'^events.json$', 'todo.views.events_json', name='events.json'),
)