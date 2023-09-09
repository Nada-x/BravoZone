from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from main.models import Achievement, Comment


# Create your views here.

def home_view(request : HttpRequest):
    
    comments = Comment.objects.all().order_by("-created_at")

    return render(request, "main/home_view.html")


def profile_detail_view(request : HttpRequest, employee_id):
    
    #to get a single entry in the database
    
    achievement = Achievement.objects.get(id=employee_id)
    comments = Comment.objects.filter(achievement=achievement)

    if request.method == "POST" and request.user.is_authenticated:
       new_comment = Comment(achievement=achievement, user=request.user, content=request.POST["content"])
       new_comment.save()

    return render(request, "main/profile.html", {"achievement" : achievement, "comments" : comments, "Comment" : Comment})

