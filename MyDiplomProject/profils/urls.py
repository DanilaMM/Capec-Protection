from django.urls import path
from .views import Render_Main, Render_Login

app_name = 'profils'

urlpatterns = [
    path('main/', Render_Main, name='main'),
    path('logun_users/', Render_Login, name='logun_users'),


]