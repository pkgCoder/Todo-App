from django.urls import path, re_path
from .views import *

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', to_do , name='todo'),
    path('<int:todo_id>/update_form/',update_form , name='update_form'),
    path('create_task/',create_form , name='create_task'),
    path('delete_todo/',delete_todo , name='delete_todo'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='todo/logout.html'), name="logout"),
    path('sign_up/',sign_up , name='sign_up'),

]