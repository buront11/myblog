from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from blog.forms import PostCreateForm

from .models import Post

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'

class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post

class PostCreateView(generic.CreateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:post_list')

class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

class PostUpdateView(generic.UpdateView):
    template_name = 'blog/post_form.html'
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(generic.DeleteView):
    tmplate_name = 'blog/post_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('blog:post_list')