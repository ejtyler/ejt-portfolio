from django.shortcuts import render
from projects.models import Project
from blog.models import Post
from drinks.models import Drink

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_on')[:3]
    projects = Project.objects.all()[:3]
    drinks = Drink.objects.all()[:3]
    context = {
        "posts": posts,
        "projects": projects,
        "drinks": drinks,
    }
    return render(request, 'home.html', context)
