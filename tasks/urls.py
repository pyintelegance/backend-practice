from django.urls import path

from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('task/<slug:slug>/', views.task_detail, name='task_detail'),
    path('task/<slug:slug>/submit/', views.submit_solution, name='submit_solution'),
    path('task/<slug:slug>/debug/', views.debug_solution, name='debug_solution'),
    path('task/<slug:slug>/buy-hint/', views.buy_hint, name='buy_hint'),
]