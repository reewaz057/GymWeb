from django.contrib import admin
from django.urls import path
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
     path('members/', views.members_list, name='members_list'),
    path('trainers/', views.trainers_list, name='trainers_list'),
    path('sessions/', views.sessions_list, name='sessions_list'),
    path('members/edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
]
