from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('tech/', views.TechAuthor.as_view(), name='tech'),
    path('author/', views.AboutAuthor.as_view(), name='author')

]
