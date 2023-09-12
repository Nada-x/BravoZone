from django.shortcuts import render, redirect
from .forms import SignUpEmployeeForm, SignUpForm, EducationalQualificationForm
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
        user_form = SignUpForm(request.POST, request.FILES)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save()
          
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
    return render(
        request,
        "accounts/signup.html",
        {"user_form": user_form},
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

def profile(request, user_id=None):
    if user_id != None:
        profile_user = User.objects.get(pk=user_id)
        print(profile_user)
    else:
        profile_user = User.objects.get(pk=request.user.id)
        print(profile_user)

    return render(request, "accounts/profile.html", { 'profile_user': profile_user })

def all_emploee(request):
    users = User.objects.filter(is_superuser=False, is_staff=False)
    return render(request, "accounts/all_employee.html")

def register_employee(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            if request.method == "POST":
                employee_form = SignUpEmployeeForm(request.POST, request.FILES)
                print(employee_form)
                if employee_form.is_valid():
                    employee = employee_form.save()
    
    return render(request, "accounts/regester.html", {"users": user})
        

# def edit_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     education_form = EducationalQualificationForm(request.POST)
#     if request.method == 'POST':
          
#         if education_form.is_valid():
#             user.first_name = request.POST.get('first_name')
#             user.last_name = request.POST.get('last_name')
#             user.bio = request.POST.get('bio')
#             user.profile_picture = request.FILES['profile_picture']
#             user.save()
#             education = education_form.save(commit=False)
#             education.user = user
#             education.save()
            
#         return redirect(f"/account/profile/{user.id}")
#     return render(request,'accounts/edit_profile.html', {'profile_id': user_id, 'profile_user': user, 'education_form': education_form})
        

def edit_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    # education_form = EducationalQualificationForm(request.POST)
    if request.method == 'POST':
          
        # if education_form.is_valid():
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.bio = request.POST.get('bio')
        # user.profile_picture = request.FILES['profile_picture']
        user.save()
            # education = education_form.save(commit=False)
            # education.user = user
            # education.save()
            
        return redirect(f"/account/profile/{user.id}")
    return render(request,'accounts/edit_profile.html', {'profile_id': user_id, 'profile_user': user})
        

# def edit_profile(request, user_id=''):
#     if user_id:
#         profile_user = User.objects.get(pk=user_id)
#     else:
#         profile_user = request.user
#         return render(request, "accounts/edit_profile.html", { 'profile_user': profile_user })

#     users = User.objects.filter(is_superuser=False, is_staff=False)

#     return render(request, "accounts/all_employee.html",{"users": users})