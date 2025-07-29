from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, "index.html")

class PostListView(ListView):
    template_name = "listpost.html"
    model = Post
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = "createpost.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('lista')

    def form_valid(self, form):
        return super().form_valid(form)