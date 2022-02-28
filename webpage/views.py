from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	DeleteView

)
from django.contrib.auth.models import User
from .models import Post




def home(request):
	context = {
	'posts': Post.objects.all()
	}
	return render(request,'webpage/home.html',context)


class PostListView(ListView):
	model = Post
	template_name = 'webpage/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] #latest_post will be at top
	paginate_by = 4

class UserPostListView(ListView):
	model = Post
	template_name = 'webpage/user_posts.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content', 'status']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content', 'status']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request,'webpage/about.html',{'title':'about'})	
	
def search(request):
	query = request.GET['query']
	if len(query)>78:
		allPosts = Post.objects.none()

	else:
		allPostsTitle = Post.objects.filter(title__icontains=query)
		allPostsContent = Post.objects.filter(content__icontains=query)
		allPosts = allPostsTitle.union(allPostsContent)
	params = {'allPosts' : allPosts}
	return render(request, 'webpage/search.html', params)