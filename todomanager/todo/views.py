from django.shortcuts import render

# -*- coding: utf-8 -*-
from django import http
from django.utils import simplejson as json
from django.utils import timezone

from todo.models import Event

def events_json(request):
    # Get all events - Pas encore terminé
    events = Event.objects.all()

    # Create the fullcalendar json events list
    event_list = []

    for event in events:
        # On récupère les dates dans le bon fuseau horaire
        event_start = event.start.astimezone(timezone.get_default_timezone())
        event_end = event.end.astimezone(timezone.get_default_timezone())

        # On décide que si l'événement commence à minuit c'est un
        # événement sur la journée
        if event_start.hour == 0 and event_start.minute == 0:
            allDay = True
        else:
            allDay = False

        if not event.is_cancelled:
            event_list.append({
                    'id': event.id,
                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                    'end': event_end.strftime('%Y-%m-%d %H:%M:%S'),
                    'title': event.title,
                    'allDay': allDay
                    })

    if len(event_list) == 0:
        raise http.Http404
    else:
        return http.HttpResponse(json.dumps(event_list),
                                 content_type='application/json')

# Create your views here.
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from todo.models import Task
#from todo.forms import TaskCreateForm



# class TaskListView(ListView):
#     """Documentation de notre controleur."""
#     model = Task
#     context_object_name = "tasks"
#     template_name = "todo/tasks-list.html"
#     paginate_by = None

# class TaskRetrieveView(DetailView):
#     model = Task
#     context_object_name = "task"
#     template_name = "todo/task.html"

# class TaskCreateView(CreateView):
#     model = Task
#     form_class = TaskCreateForm
#     template_name = "todo/task-create.html"

#     def get_initial(self):
#         return self.initial.copy()

# class TaskUpdateView(UpdateView):
#     model = Task
#     form_class = TaskCreateForm
#     template_name = "todo/task-create.html"

# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = "todo/task-delete.html"
#     success_url = '/'

