from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path(r'', views.PostList.as_view(), name='all'),
    path(r'new/', views.CreatePost.as_view(), name='create'),
    path(r'by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path(r'by/<username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path(r'delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]