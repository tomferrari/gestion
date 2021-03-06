from django.shortcuts import render

##TEST CONNEXION
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView, ListView
from django.conf import settings
#from .models import Reservation
from todo.models import Reservation

class LoginView(TemplateView):
    template_name = 'front/index.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name)

class LogoutView(TemplateView):
    template_name = 'front/index.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
#END Modif

class reservationView(TemplateView):
    template_name = 'backoffice/listsReservations.html'
    model = Reservation
    
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
