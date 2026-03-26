import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project1.settings')
django.setup()

from blog.models import Post
from django.contrib.auth.models import User

# Ensure users with id 1 and 2 exist
if not User.objects.filter(id=1).exists():
    User.objects.create_user(id=1, username='admin', password='password', email='admin@test.com')
if not User.objects.filter(id=2).exists():
    User.objects.create_user(id=2, username='testuser', password='password', email='test@test.com')

with open('django_project1/posts.json') as f:
    posts_json = json.load(f)

for post_data in posts_json:
    Post.objects.create(
        title=post_data['title'],
        content=post_data['content'],
        author_id=post_data['user_id']
    )
print("Posts loaded successfully!")
