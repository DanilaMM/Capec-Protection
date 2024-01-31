from django.http import HttpRequest
from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views, login, authenticate


def Render_Main(request):
    return render(request, 'profils/main.html')


def Render_Login(request: HttpRequest):
    if request.method == 'POST':
        form = request.POST
        user = authenticate(username=form['login'], password=form['password'])
        if user:
            login(request, user)
            return render(request,'profils/glavn_str.html')
        else:
            return render(request, 'profils/logun_users.html')

    else:
        return render(request, 'profils/logun_users.html')




