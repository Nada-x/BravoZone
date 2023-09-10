from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # path('', views.home_view, name="home_view"),
    # path('profile/', views.profile_detail_view, name="profile_detail_view"),
    path('add_previous_project/', views.add_previous_project, name='add_previous_project'),
    path('add_comment/<int:project_id>/', views.add_comment, name='add_comment'),
]
