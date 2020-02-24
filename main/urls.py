from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('sign-up/', views.signup_view, name='sign_up')
]
