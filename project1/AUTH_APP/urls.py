from django.urls import path
from .import views

urlpatterns = [
    path('rv/', views.registerView, name='register_url'),
    path('lv/', views.loginView, name='log_url'),
    path('lgv/', views.logoutView, name='logout_url')
]