from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, UserProfile, Comment, Tour, Worker, Message, NearestDate, Day, Country, City, HotTour
from .forms import PostForm, UserForm, UserProfileForm, CommentForm, WorkerForm, MessageForm, ToursForm, NearestDateForm, DayForm, CountryForm, CityForm, HotTourForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, update_session_auth_hash
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
    return render(request, 'worldtravelapp/admin/sign_up.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form
        })

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_room(request):
    return redirect('admin_orders')


@login_required(login_url='/auth/sign-in/')
def admin_orders(request):
    return render(request, 'worldtravelapp/admin/admin_orders.html', {})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours(request):
    tours = Tour.objects.all().order_by('title')
    return render(request, 'worldtravelapp/admin/admin_tours.html', {'tours': tours})



@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_new(request):
    if request.method == "POST":
        tours_form = ToursForm(request.POST, request.FILES)
        if tours_form.is_valid():
            tours_form.save()
            return redirect('admin_tours')
    else:
        tours_form = ToursForm()
    return render(request, 'worldtravelapp/admin/admin_tours_new.html', {'tours_form': tours_form})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_edit(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    nearestdates = NearestDate.objects.filter(tour=tour)
    days = Day.objects.filter(tours_list=tour).order_by('number')
    if request.method == "POST":
        tours_form = ToursForm(request.POST, request.FILES, instance=tour)
        if tours_form.is_valid():
            tours_form.save()
            return redirect('admin_tours')
    else:
        tours_form = ToursForm(instance=tour)
    return render(request, 'worldtravelapp/admin/admin_tours_edit.html', {
        'tours_form': tours_form, 
        'nearestdates' : nearestdates, 
        'tour':tour, 
        'days':days})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_edit_date(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == "POST":
        dates_form = NearestDateForm(request.POST)
        if dates_form.is_valid():
            new_date = dates_form.save(commit=False)
            new_date.tour = tour
            new_date.save()
            return redirect('admin_tours_edit', pk=tour.pk)
    else:
        dates_form = NearestDateForm()
    return render(request, 'worldtravelapp/admin/admin_tours_edit_date.html', {'dates_form' : dates_form})

@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_date_remove(request, pk):
    date = get_object_or_404(NearestDate, pk=pk)
    date.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_day_new(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    if request.method == "POST":
        days_form = DayForm(request.POST)
        if days_form.is_valid():
            new_day = days_form.save(commit=False)
            new_day.tours_list = tour
            new_day.save()
            return redirect('admin_tours_edit', pk=tour.pk)
    else:
        days_form = DayForm()
    return render(request, 'worldtravelapp/admin/admin_tours_edit_day.html', {'days_form' : days_form})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_day_edit(request, pk):
    day = get_object_or_404(Day, pk=pk)
    tour = get_object_or_404(Tour, pk=day.tours_list.pk)
    if request.method == "POST":
        days_form = DayForm(request.POST, instance=day)
        if days_form.is_valid():
            days_form.save()
            return redirect('admin_tours_edit', pk=tour.pk)
    else:
        days_form = DayForm(instance=day)
    return render(request, 'worldtravelapp/admin/admin_tours_edit_day.html', {'days_form' : days_form})

@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_day_remove(request, pk):
    day = get_object_or_404(Day, pk=pk)
    day.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@permission_required('worldtravelapp.add_post', login_url='/')
def admin_tours_remove(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    tour.delete()
    return redirect('admin_tours')




@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_workers(request):
    workers = Worker.objects.all().order_by('first_name')
    return render(request, 'worldtravelapp/admin/admin_workers.html', {'workers': workers})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_workers_new(request):
    workers = Worker.objects.all().order_by('first_name')
    if request.method == "POST":
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_workers')
    else:
        form = WorkerForm()
    return render(request, 'worldtravelapp/admin/admin_workers_new.html', {'workers': workers, 'form': form})


@login_required(login_url='/auth/sign-in/')
def admin_workers_edit(request, pk):
    workers = Worker.objects.exclude(pk=pk).order_by('first_name')
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        form = WorkerForm(request.POST, request.FILES, instance=worker)
        if form.is_valid():
            worker = form.save()
            return redirect('admin_workers')
    else:
        form = WorkerForm(initial={'first_name': worker.first_name, 'last_name': worker.last_name, 'job': worker.job})
    return render(request, 'worldtravelapp/admin/admin_workers_new.html', {'workers': workers, 'form': form})


@permission_required('worldtravelapp.add_post', login_url='/')
def admin_workers_remove(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    worker.delete()
    return redirect('admin_workers')


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_countrys(request):
    countrys = Country.objects.all().order_by('title')
    return render(request, 'worldtravelapp/admin/admin_countrys.html', {'countrys': countrys})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_countrys_new(request):
    countrys = Country.objects.all().order_by('title')
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_countrys')
    else:
        form = CountryForm()
    return render(request, 'worldtravelapp/admin/admin_countrys_new.html', {'countrys': countrys, 'form': form})


@login_required(login_url='/auth/sign-in/')
def admin_countrys_edit(request, pk):
    countrys = Country.objects.exclude(pk=pk).order_by('title')
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            country = form.save()
            return redirect('admin_countrys')
    else:
        form = CountryForm(initial={'title': country.title, 'continent': country.continent, 'pk': country.pk})
    return render(request, 'worldtravelapp/admin/admin_countrys_new.html', {'country': country, 'countrys': countrys, 'form': form})


@permission_required('worldtravelapp.add_post', login_url='/')
def admin_countrys_remove(request, pk):
    country = get_object_or_404(Country, pk=pk)
    country.delete()
    return redirect('admin_countrys')


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_citys(request):
    citys = City.objects.all().order_by('title')
    return render(request, 'worldtravelapp/admin/admin_citys.html', {'citys': citys})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_citys_new(request):
    citys = City.objects.all().order_by('title')
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_citys')
    else:
        form = CityForm()
    return render(request, 'worldtravelapp/admin/admin_citys_new.html', {'citys': citys, 'form': form})


@login_required(login_url='/auth/sign-in/')
def admin_citys_edit(request, pk):
    citys = City.objects.exclude(pk=pk).order_by('title')
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES, instance=city)
        if form.is_valid():
            city = form.save()
            return redirect('admin_citys')
    else:
        form = CityForm(initial={'title': city.title, 'country': city.country, 'pk': city.pk})
    return render(request, 'worldtravelapp/admin/admin_citys_edit.html', {'city': city, 'citys': citys, 'form': form})


@permission_required('worldtravelapp.add_post', login_url='/')
def admin_citys_remove(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('admin_citys')



@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_hottours(request):
    hottours = HotTour.objects.all().order_by('tour')
    return render(request, 'worldtravelapp/admin/admin_hottours.html', {'hottours': hottours})

@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_hottours_new(request):
    hottours = HotTour.objects.all().order_by('tour')
    if request.method == "POST":
        form = HotTourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_hottours')
    else:
        form = HotTourForm()
    return render(request, 'worldtravelapp/admin/admin_hottours_new.html', {'hottours': hottours, 'form': form})


@login_required(login_url='/auth/sign-in/')
def admin_hottours_edit(request, pk):
    hottours = HotTour.objects.exclude(pk=pk).order_by('tour')
    hottour = get_object_or_404(HotTour, pk=pk)
    if request.method == "POST":
        form = HotTourForm(request.POST, request.FILES, instance=hottour)
        if form.is_valid():
            hottour = form.save()
            return redirect('admin_hottours')
    else:
        form = HotTourForm()
    return render(request, 'worldtravelapp/admin/admin_hottours_new.html', {'hottour': hottour, 'hottours': hottours, 'form': form})


@permission_required('worldtravelapp.add_post', login_url='/')
def admin_hottours_remove(request, pk):
    hottour = get_object_or_404(HotTour, pk=pk)
    hottour.delete()
    return redirect('admin_hottours')



@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_messages(request):
    messages = Message.objects.all().order_by('-created_date')
    return render(request, 'worldtravelapp/admin/admin_messages.html', {'messages': messages})

@permission_required('worldtravelapp.add_post', login_url='/')
def admin_messages_remove(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.delete()
    return redirect('admin_messages')


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_news(request):
    return redirect('admin_news_ok')


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_news_ok(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'worldtravelapp/admin/admin_news_ok.html', {'posts': posts})


@login_required(login_url='/auth/sign-in/')
@permission_required('worldtravelapp.add_post', login_url='/')
def admin_news_draft(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'worldtravelapp/admin/admin_news_draft.html', {'posts': posts})








@login_required(login_url='/auth/sign-in/')
def user_room(request):
    return redirect('user_mytours')


@login_required(login_url='/auth/sign-in/')
def user_order(request):
    return render(request, 'worldtravelapp/user/user_order.html', {})


@login_required(login_url='/auth/sign-in/')
def user_history(request):
    return render(request, 'worldtravelapp/user/user_history.html', {})

@login_required(login_url='/auth/sign-in/')
def user_desire(request):
    return render(request, 'worldtravelapp/user/user_desire.html', {})


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
            return redirect('user_settings')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)
        password_form = PasswordChangeForm(request.user)
    return render(request, 'worldtravelapp/user/user_settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form
        })




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'worldtravelapp/news/news.html', {'posts': posts})


def post_detail(request, pk):
    dates = Tour.objects.get(pk=1)
    comments = Comment.objects.filter(post=pk)
    post = get_object_or_404(Post, pk=pk)
    post.tags = post.tags.split(',')
    form = CommentForm()
    return render(request, 'worldtravelapp/news/news_detail.html', {'post': post, 'dates': dates, 'comments': comments, 'form': form})


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
    return render(request, 'worldtravelapp/news/news_edit.html', {'form': form})


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
    return render(request, 'worldtravelapp/news/news_edit.html', {'form': form})


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
    return render(request, 'worldtravelapp/other/about_us.html', {'workers': workers})


def contacts(request):
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = MessageForm()
    return render(request, 'worldtravelapp/other/contacts.html', {'form': form})