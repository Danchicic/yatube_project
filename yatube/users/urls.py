from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'),
         name='change_password'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='change_password_done'),

    # path('login/', LoginView.as_view(template_name='users/../templates/registration/login.html'), name='login'),
]
