from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluation:task_list')
    else:
        form = TaskForm()
    return render(request, 'evaluation/task_create.html', {'form': form})



def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'evaluation/task_list.html', {'tasks': tasks})