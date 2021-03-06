"""
URL configuration to process register, login, logout and account pages.
"""
from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('account/', views.account, name="account"),
]
