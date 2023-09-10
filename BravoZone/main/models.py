from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from account.models import User
from django.conf import settings


class PreviousProject(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='previous_projects/')
    link = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    project = models.ForeignKey(PreviousProject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.project.title}"


