from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import path
from django.views import View
from .models import User, Projcets
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
        User.objects.create_user(username=request.POST['login'], password=request.POST['password'],
                                 email=request.POST['mail'])
        return render(request, 'profils/logun_users.html')

    def get(self, request):
        return render(request, 'profils/registration.html')



@login_required(login_url='profils:logun_users')
def MyAccount(request):
    return render(request,'profils/my_account.html')

@login_required(login_url='profils:logun_users')
def Projects(request):
    return render(request,'profils/my_projects.html')


@login_required(login_url='profils:logun_users')
def Create_project(request):
    Projects.objects.create(is_wireless_tech=request.POST['is_wireless_tech'],
                            is_cloud_tech=request.POST['is_cloud_tech'],
                            is_virtual_tech=request.POST['is_virtual_tech'],
                            protection_class=request.POST['protection_class'],
                            user_id=request.user.id)

    # is_wireless_tech = models.BooleanField()
    # is_cloud_tech = models.BooleanField()
    # is_virtual_tech = models.BooleanField()
    # protection_class = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)