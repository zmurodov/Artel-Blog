from django.contrib.auth import authenticate, login

from .forms import SignUpForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'main/home.html', {})


def home_view(request):
    return render(request, 'main/home.html')


def signup_view(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     print(request.POST)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         print('valid')
    #         user = form.save()
    #         user.refresh_from_db()
    #         user.profile.first_name = form.cleaned_data.get('first_name')
    #         user.profile.last_name = form.cleaned_data.get('last_name')
    #         user.profile.email = form.cleaned_data.get('email')
    #         user.save()
    #         print(user)
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         print('login')
    #         return redirect('/home')
    # else:
    #     form = SignUpForm()
    # return render(request, 'main/signup_view.html', {'form': form})
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            context = {
                'name': name,
                'email': email,
                'password': password
            }
            return redirect('/home', context=context)
        else:
            return HttpResponse('form is invalid')
    else:
        form = SignUpForm()
        return render(request, 'main/sign_up.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'main/login.html', {})
