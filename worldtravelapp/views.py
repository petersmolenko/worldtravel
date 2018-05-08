from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, UserProfile
from .forms import PostForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def sign_up(request):
    user_form = UserForm()
    user_profile_form = UserProfileForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_profile = user_profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
                ))
            return redirect('/')
    return render(request, 'admin/sign_up.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form
        })

@login_required(login_url='/auth/sign-in/')
def admin_news(request):
    return redirect('admin_news_ok')

@login_required(login_url='/auth/sign-in/')
def admin_news_ok(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'admin/admin_news_ok.html', {'posts': posts})

@login_required(login_url='/auth/sign-in/')
def admin_news_draft(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'admin/admin_news_draft.html', {'posts': posts})

@login_required(login_url='/auth/sign-in/')
def admin_tours(request):
    return render(request, 'admin/admin_tours.html', {})
    
@login_required(login_url='/auth/sign-in/')
def admin_mytours(request):
    return render(request, 'admin/admin_mytours.html', {})
    
@login_required(login_url='/auth/sign-in/')
def admin_comments(request):
    return render(request, 'admin/admin_comments.html', {})
    
@login_required(login_url='/auth/sign-in/')
def admin_orders(request):
    return render(request, 'admin/admin_orders.html', {})
    
@login_required(login_url='/auth/sign-in/')
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
            post.save()
            return redirect('admin_news_draft', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/news_edit.html', {'form': form})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('admin_news', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('admin_news')

@login_required(login_url='/auth/sign-in/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('admin_news')
    else:
        form = PostForm(instance=post)
    return render(request, 'news/news_edit.html', {'form': form})
