from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    template_name = 'blog/post_form.html'  # Template for the form
    fields = ['title', 'content']          # Fields displayed in the form
    success_url = reverse_lazy('blog-home')  # Redirect after submit

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Optional function-based views
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})