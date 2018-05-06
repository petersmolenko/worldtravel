from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def admin_news(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'admin/admin_news.html', {'posts': posts})

def admin_tours(request):
    return render(request, 'admin/admin_tours.html', {})

def admin_orders(request):
    return render(request, 'admin/admin_orders.html', {})

def admin_settings(request):
    return render(request, 'admin/admin_settings.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news/news.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.tags = post.tags.split(',')
    return render(request, 'news/news_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/news_edit.html', {'form': form})
  
@login_required(login_url='/auth/login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('admin_news')
    else:
        form = PostForm(instance=post)
    return render(request, 'news/news_edit.html', {'form': form})