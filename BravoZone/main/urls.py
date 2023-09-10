from django.urls import path
from . import views

app_name= "main"

urlpatterns=[
    path('' , views.home_view, name= "home_view"),
    path('profile/' , views.profile_detail_view, name="profile_detail_view")
]

