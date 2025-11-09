from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # 👈 Usa tu vista personalizada
    path('logout/', views.logout_view, name='logout'),  # 👈 Usa tu logout personalizado
    path('register/', views.register, name='register')
]