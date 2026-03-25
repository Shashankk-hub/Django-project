from django.urls import path
from . import views

urlpatterns = [
    # Home / List of posts
    path('', views.PostListView.as_view(), name='blog-home'),
    
    # Detail view for a single post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    
    # Create a new post (requires logged-in user)
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    
    # Update an existing post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    
    # Delete an existing post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
    # About page
    path('about/', views.about, name='about-page'),
]