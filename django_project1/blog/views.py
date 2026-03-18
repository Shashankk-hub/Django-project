from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView

class PostListView(ListView):
       model = Post
       template_name = 'blog/home.html'
       context_object_name = 'posts'
       ordering = ['-date_posted']
       
       

def home(request):
   context = {
   'posts': Post.objects.all()
   }
   return render(request, 'blog/home.html', context)

# def home(request):
#    context = {
#    'posts': posts
#    }
   
def about(request):
   return render(request, 'blog/about.html', {'title': 'About'})


# posts = [
# {
#    'author': 'shashank',
#    'title': 'Blog Post 1',
#    'content': 'Blog 1 Content!',
#    'date_posted': 'January 20, 2026'
# },
# {
#    'author': 'aryan',
#    'title': 'Blog Post 2',
#    'content': 'Blog 2 Content!',
#    'date_posted': 'January 23, 2026'
# }
# ]