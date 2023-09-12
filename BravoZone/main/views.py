from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .forms import PreviousProjectForm, CommentForm
from .models import PreviousProject, Comment

import sys

sys.path.append(".")
from evaluation.models import Task
from account.models import User


def home_view(request: HttpRequest):
    comments = Comment.objects.all().order_by("-created_at")

    return render(request, "main/home_view.html")


def add_previous_project(request):
    if request.method == "POST":
        form = PreviousProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("previous_projects")
    else:
        form = PreviousProjectForm()
    return render(request, "main/add_previous_project.html", {"form": form})


def add_comment(request, project_id):
    project = get_object_or_404(PreviousProject, pk=project_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.user = request.user
            comment.save()
            return redirect("project_detail", project_id=project_id)
    else:
        form = CommentForm()
    return render(request, "main/add_comment.html", {"form": form, "project": project})


def leader_bord(request):
    employees = User.objects.filter(is_superuser=False, is_staff=False)
    
    leaderboard_list = []
    for employee in employees:
        employee_tasks = Task.objects.filter(assigned_to=employee)
        print(employee_tasks)
        # leaderboard_list.append({'employee': employee})
    return render(request, "main/leader_bord.html")
