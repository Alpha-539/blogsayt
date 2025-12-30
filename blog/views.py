from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title','body','author','slug']
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title','body','slug']
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')