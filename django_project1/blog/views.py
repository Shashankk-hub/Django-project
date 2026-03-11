from django.shortcuts import render
from blog.models import Post

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
#    'author': 'Aryan',
#    'title': 'Blog Post 1',
#    'content': 'Blog 1 Content!',
#    'date_posted': 'January 20, 2026'
# },
# {
#    'author': 'Ramu',
#    'title': 'Blog Post 2',
#    'content': 'Blog 2 Content!',
#    'date_posted': 'January 23, 2026'
# }
# ]