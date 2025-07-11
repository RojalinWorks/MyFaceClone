from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('signout/', views.signout, name='logout'),
    path('register/', views.register, name='register'),
    path('update_profile/', views.update_profile, name='update'),
    path('create_post/', views.create_post, name='addpost'),
]
