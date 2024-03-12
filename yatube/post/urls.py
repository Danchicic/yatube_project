from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name="main"),
    path('group/<slug:group_name>/', views.group_posts, name='group'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.CreatePostView.as_view(), name='post_create'),
    path("posts/<int:post_id>/edit/", views.EditPostView.as_view(), name="post_update"),
]
