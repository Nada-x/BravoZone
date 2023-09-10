from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
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
        form = TaskForm(initial={'assigned_to': request.GET['assigned_to']})
    return render(request, 'evaluation/task_create.html', {'form': form})


def task_list(request):
    all_tasks = None
    if request.user.is_superuser:
        all_tasks = Task.objects.all()
    return render(request, 'evaluation/task_list.html', {'all_tasks': all_tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.update_status() 
    return render(request, 'evaluation/task_detail.html', {'task': task})


def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
            
        return redirect('evaluation:task_detail', task_id=task_id)