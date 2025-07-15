from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
def home(request):
    return render(request, "index.html")

class PostListView(ListView):
    template_name = "listpost.html"
    model = Post
    context_object_name = 'posts'