from django.shortcuts import render
from projects.models import Project
from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_on')[:3]
    projects = Project.objects.all()
    context = {
        "posts": posts,
        "projects": projects,
    }
    return render(request, 'home.html', context)