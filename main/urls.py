from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('sign-up/', views.signup_view, name='sign_up')
]
