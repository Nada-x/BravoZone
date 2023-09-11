from django.shortcuts import render, redirect
from .forms import SignUpForm, EducationalQualificationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import User
from django.contrib.auth import logout


def home(request):
    # users = User.objects.all()
    users = User.objects.filter(is_superuser=False, is_staff=False)
    return render(request, "accounts/home.html", {"users": users})


def signup(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        qualification_form = EducationalQualificationForm(request.POST, request.FILES)
        if user_form.is_valid() and qualification_form.is_valid():
            user = user_form.save()
            qualification = qualification_form.save(commit=False)
            qualification.user = user
            qualification.save()

            role = user_form.cleaned_data["role"]
            if role == "admin":
                user.is_staff = True
            elif role == "superadmin":
                user.is_staff = True
                user.is_superuser = True
            user.save()
            return redirect("account:login")
    else:
        user_form = SignUpForm()
        qualification_form = EducationalQualificationForm()
    return render(
        request,
        "accounts/signup.html",
        {"user_form": user_form, "qualification_form": qualification_form},
    )
 

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("account:home")
                else:
                    form.add_error(None, "Invalid username or password.")
        else:
            form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})
    return redirect("account:profile")


def logout_view(request):
    logout(request)
    return redirect("account:login")

def profile(request, user_id=''):
    if user_id:
        profile_user = User.objects.get(pk=user_id)
    else:
        profile_user = request.user
    return render(request, "accounts/profile.html", { 'profile_user': profile_user })
        