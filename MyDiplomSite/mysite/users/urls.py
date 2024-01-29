from django.urls import path
from views import profile_view

app_name = 'profile'

urlpatterns = [
    path('login/', profile_view, name='profile'),
    #path('logout/', views.logout_user, name='logout'),
]