from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news/news.html', {'posts': posts})

def admin_news(request):
    return render(request, 'admin/admin_news.html', {})

def admin_tours(request):
    return render(request, 'admin/admin_tours.html', {})

def admin_orders(request):
    return render(request, 'admin/admin_orders.html', {})

def admin_settings(request):
    return render(request, 'admin/admin_settings.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.tags = post.tags.split(',')
    return render(request, 'news/news_detail.html', {'post': post})