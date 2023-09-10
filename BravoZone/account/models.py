from django.db import models
from django.contrib.auth.models import AbstractUser
    
class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    employee_number = models.CharField(max_length=20)
    email = models.EmailField()
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.username

class EducationalQualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True ,null=True , related_name='education')
    university_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    academic_rank = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures')

    def __str__(self):
        return self.user.username