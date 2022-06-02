"""posts views."""
#django
from pdb import post_mortem
from re import template
from wsgiref.util import request_uri
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView,ListView
from django.http import HttpResponse

#Forms
from posts.forms import PostForm

from posts.models import Post

#utilities
from datetime import datetime

class PostsFeedView(LoginRequiredMixin, ListView):
	"""Return all published posts."""
	template_name= 'posts/feed.html'
	model= Post
	ordering=('-created',)
	paginate_by = 20
	context_object_name= 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
	"""Return post detail"""
	template_name='posts/detail.html'
	queryset= Post.objects.all()
	context_object_name='post'

class CreatePostView(LoginRequiredMixin, CreateView):
	"""Create a new Post view."""
	template_name= 'posts/new.html'
	form_class = PostForm
	success_url= reverse_lazy('posts:feed')
	
	def get_context_data(self, **kwargs):
		"""Add user and profile to context."""
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context


