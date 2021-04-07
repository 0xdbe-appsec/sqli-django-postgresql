from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection

from .models import Task
from .forms import TaskForm

def task_list(request):
    user = request.GET.get('user', "me")
    # hack
    #user = "me' OR 1=1--"
    query = "SELECT * from sqli_task WHERE owner = %s"
    cursor = connection.cursor()
    cursor.execute(query, [user])
    tasks = cursor.fetchall()
    data = {
        'tasks': tasks
    }
    return render(
        request,
        'tasklist.html',
        data
    )

def task_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')
    else:
      form = TaskForm
      return render(request, 'task_form.html', {'form': form})
