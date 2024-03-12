from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('new_book/', views.NewBookView.as_view(), name='new_book'),
    path('book/<slug:book_name>', views.LibraryBookView.as_view()),
    path('', views.LibraryMainView.as_view(), name='main'),
    path("rock/", views.UserCd.as_view(), name='rock')

]
