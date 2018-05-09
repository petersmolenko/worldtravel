from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, UserProfile, Comment
from .forms import PostForm, UserForm, UserProfileForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
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
@permission_required('worldtravelapp.add_post', login_url='/')
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
    comments = Comment.objects.filter(post=pk)
    post = get_object_or_404(Post, pk=pk)
    post.tags = post.tags.split(',')
    form = CommentForm()
    return render(request, 'news/news_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('admin_news_draft')
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

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)