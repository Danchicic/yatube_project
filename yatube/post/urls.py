from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name="main"),
    path('group/<slug:group_name>/', views.group_posts, name='group')
]
