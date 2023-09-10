from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Skill, User, EducationalQualification

class SignUpForm(UserCreationForm):
    ROLE_CHOICES=(
        ('admin', 'Admin'),
        ('superadmin','Super Admin'),
        ('user','User'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'employee_number', 'email', 'skills','role']

class EducationalQualificationForm(forms.ModelForm):
    class Meta:
        model = EducationalQualification
        fields = ['university_name', 'major', 'degree', 'academic_rank', 'profile_picture']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


