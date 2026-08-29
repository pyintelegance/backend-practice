from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/jump-level/', views.jump_level, name='jump_level'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/<int:user_id>/toggle-staff/', views.toggle_staff, name='toggle_staff'),
]