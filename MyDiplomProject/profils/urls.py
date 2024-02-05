from django.urls import path
from .views import Render_Main, UserLoginView, UserLogoutView, Render_glavn, Registration, MyAccount

app_name = 'profils'

urlpatterns = [
    path('main/', Render_Main, name='main'),
    path('logun_users/', UserLoginView.as_view(), name='logun_users'),
    path('logout_users/', UserLogoutView.as_view(), name='logout_users'),
    path('glavn_str/', Render_glavn, name='rend_glavn'),
    path('registration/', Registration.as_view(), name='Registration'),
    path('my_account/', MyAccount, name='MyAccount')


]