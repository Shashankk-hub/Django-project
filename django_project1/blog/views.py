from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post

# Home / List view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Template for the list
    context_object_name = 'posts'
    ordering = ['-date_posted']       # newest first

# Detail view for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create view for a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content']          
    success_url = reverse_lazy('blog-home')  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# Update view for a single post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content']          
    success_url = reverse_lazy('blog-home')  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Delete view for a single post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Optional function-based views
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})