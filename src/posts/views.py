from django.shortcuts import render
from .models import Post
# Create your views here.

#CRUD views

# List all posts in a view


def post_list_view(request):
	# Must also reference objects in context{} 
    post_objects = Post.objects.all()
    context = {
        'post_objects': post_objects
    }
    # posts/index.html => 'Inside /posts, look for index.html'
    return render(request, "posts/index.html", context)