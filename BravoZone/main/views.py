from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main.models import Achievement, Comment


# Create your views here.

def home_view(request : HttpRequest):
    
    comments = Comment.objects.all().order_by("-created_at")

    return render(request, "main/home_view.html")


def profile_detail_view(request : HttpRequest):
    
   
    return render(request, "main/profile.html")

