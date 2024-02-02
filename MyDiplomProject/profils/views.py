from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import path
from django.views import View
from .models import User
from . import views
from django.contrib.auth import views as auth_views, login, authenticate, logout


def Render_Main(request):
    return render(request, 'profils/main.html')

@login_required(login_url='profils:logun_users')
def Render_glavn(request):
    return render(request, 'profils/glavn_str.html')


class UserLoginView(View):

    def post(self, request):
        user = authenticate(username=request.POST['login'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('profils:rend_glavn')
        return render(request, 'profils/logun_users.html')

    def get(self, request):
        return render(request, 'profils/logun_users.html')
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('profils:main')

class Registration(View):

    def post(self, request):
        User.objects.create(username=request.POST['login'], password=request.POST['password'])
        return render(request, 'profils/logun_users.html')

    def get(self, request):
        return render(request, 'profils/registration.html')





