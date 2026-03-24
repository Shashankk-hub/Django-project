from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('about/', views.about, name='about-page'),
      # Home / List of posts
    path('', views.PostListView.as_view(), name='blog-home'),
    
    # Detail view for a single post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    
    # Create a new post (requires logged-in user)
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    
    # About page
    path('about/', views.about, name='about-page'),
]