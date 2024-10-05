from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model =Post
    
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model=Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='app1/post_detail.html'
    form_class=PostForm
    model=Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='app1/post_detail.html'
    form_class=PostForm
    model=Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name = 'app1/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date_isnull=True).order_by('created_date')