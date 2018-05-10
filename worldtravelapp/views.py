from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, UserProfile, Comment, Tour, Worker
from .forms import PostForm, UserForm, UserProfileForm, CommentForm, WorkerForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



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
def admin_room(request):
    return redirect('admin_orders')


@login_required(login_url='/auth/sign-in/')
def admin_orders(request):
    return render(request, 'admin/admin_orders.html', {})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours(request):
    return render(request, 'admin/admin_tours.html', {})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_workers(request):
    workers = Worker.objects.all().order_by('first_name')
    return render(request, 'admin/admin_workers.html', {'workers': workers})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_workers_new(request):
    workers = Worker.objects.all().order_by('first_name')
    if request.method == "POST":
        workers_form = WorkerForm(request.POST, request.FILES)
        if workers_form.is_valid():
            workers_form.save()
            return redirect('admin_workers')
    else:
        workers_form = WorkerForm()
    return render(request, 'admin/admin_workers_new.html', {'workers': workers, 'workers_form': workers_form})


@login_required(login_url='/auth/sign-in/')
def admin_workers_edit(request, pk):
    workers = Worker.objects.exclude(pk=pk).order_by('first_name')
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        workers_form = WorkerForm(request.POST, request.FILES, instance=worker)
        if workers_form.is_valid():
            worker = workers_form.save()
            return redirect('admin_workers')
    else:
        workers_form = WorkerForm(initial={'first_name': worker.first_name, 'last_name': worker.last_name, 'job': worker.job})
    return render(request, 'admin/admin_workers_edit.html', {'workers': workers, 'workers_form': workers_form})


@permission_required('worldtravelapp.add_post', login_url='/')
def admin_workers_remove(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    worker.delete()
    return redirect('admin_workers')

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_messages(request):
    return render(request, 'admin/admin_messages.html', {})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_news(request):
    return redirect('admin_news_ok')


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_news_ok(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'admin/admin_news_ok.html', {'posts': posts})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_news_draft(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'admin/admin_news_draft.html', {'posts': posts})








@login_required(login_url='/auth/sign-in/')
def user_room(request):
    return redirect('user_mytours')


@login_required(login_url='/auth/sign-in/')
def user_mytours(request):
    return render(request, 'user/user_mytours.html', {})


@login_required(login_url='/auth/sign-in/')
def user_comments(request):
    return render(request, 'user/user_comments.html', {})


@login_required(login_url='/auth/sign-in/')
def user_settings(request):
    user = request.user
    #---------To created in console users--------
    if not UserProfile.objects.filter(user=user):
        profile_form = UserProfileForm()
        new_profile = profile_form.save(commit=False)
        new_profile.user = request.user
        new_profile.save()
    #---------------------------------------------
    user_profile = UserProfile.objects.get(user=user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        password_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            user_profile = profile_form.save()
            user_profile.save()
            if password_form.is_valid():
                password_user = password_form.save()
                update_session_auth_hash(request, password_user)
                messages.success(request, 'Ваш пароль успешно изменен!')
            else:
                messages.error(request, 'Исправьте ошибки!')
            return redirect('user_settings')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'user/user_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form
        })




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'news/news.html', {'posts': posts})


def post_detail(request, pk):
    dates = Tour.objects.get(pk=1)
    comments = Comment.objects.filter(post=pk)
    post = get_object_or_404(Post, pk=pk)
    post.tags = post.tags.split(',')
    form = CommentForm()
    return render(request, 'news/news_detail.html', {'post': post, 'dates': dates, 'comments': comments, 'form': form})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
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


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('admin_news')


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
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


@login_required(login_url='/auth/sign-in/')
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




@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.delete_comment', login_url='/')
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@permission_required('worldtravelapp.delete_comment', login_url='/')
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def about_us(request):
    workers = Worker.objects.order_by('first_name')
    return render(request, 'other/about_us.html', {'workers': workers})