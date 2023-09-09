from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Achievement(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    link = models.URLField(blank=True)
    Achievement_date = models.DateField(default="2000-10-10")
    
    
class Comment(models.Model):
    
    
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} on {self.achievement.title}"
    
    
    
  
    
        

    



