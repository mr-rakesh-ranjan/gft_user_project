from turtle import update
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_user, name='add-user'),
    path('all/', views.all_users, name='all_users'),
    path('update/<int:userId>/', views.update_user, name='update-user' ),
    path('user/<int:userId>/delete', views.delete_user, name='delete-user'),
    path('user/<int:userId>', views.get_userById, name='user-by-Id')
]
