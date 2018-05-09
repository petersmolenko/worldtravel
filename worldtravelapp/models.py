from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='users/', blank=True, verbose_name='Фото профиля')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
 
    def __unicode__(self):
        return self.user

    @property
    def photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Tour(models.Model):
    TYPE_TOUR_CHOICES = (
        ('EXC', 'Экскурсионный'),
        ('BEA', 'Пляжный'),
        ('WEE', 'Выходного дня'),
        ('ACT', 'Активный'),
    )
    type_tour = models.CharField(max_length=3, choices=TYPE_TOUR_CHOICES, default='EXC', verbose_name='Тип тура')
    duration = models.IntegerField(verbose_name='Продолжительность')
    price = models.FloatField(verbose_name='Цена')
    cities = models.CharField(max_length=200, verbose_name='Города')
    countries = models.CharField(max_length=200, verbose_name='Страны')
    title = models.CharField(max_length=200, verbose_name='Название тура')
    text = models.TextField(verbose_name='Описание тура')
    nearest_date = models.ManyToManyField('worldtravelapp.NearestDate', related_name='tours', verbose_name='Ближайшие даты', blank=True)
    photo = models.ImageField(upload_to='tours/', blank=True, default='', verbose_name='Фото тура')

    
    class Meta:
        verbose_name='Тур'
        verbose_name_plural='Туры'
        ordering=['title']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
        
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title

class NearestDate(models.Model):
    tours_list = models.ManyToManyField('worldtravelapp.Tour', related_name='dates', verbose_name='Туры', blank=True)
    date = models.DateField(default=timezone.now, verbose_name='Дата тура')

    class Meta:
        verbose_name='Дата тура'
        verbose_name_plural='Даты туров'

    def __str__(self):
        return str(self.date)



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short_descript = models.CharField(max_length=300, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Текст статьи')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='news_images/', blank=True, default='', verbose_name='Фото к статье')
    tags = models.CharField(max_length=100, verbose_name='Тэги')

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'
        ordering=['created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
        
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('worldtravelapp.Post', related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    approved_comment = models.BooleanField(default=False, verbose_name='Одобренный комментарий')

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Message(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(max_length=40, verbose_name='E-mail')
    message = models.TextField(verbose_name='Сообщение')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural='Сообщения'

    def __str__(self):
        return self.message


class Worker(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    job = models.CharField(max_length=40, verbose_name='Должность')
    photo = models.ImageField(upload_to='news_images/', blank=True, default='', verbose_name='Фото сотрудника')

    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.last_name

class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    tour = models.ForeignKey('worldtravelapp.Tour', related_name='reviews', on_delete=models.CASCADE, verbose_name='Тур')
    text = models.TextField(verbose_name='Отзыв')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    approved_reviews = models.BooleanField(default=False, verbose_name='Одобренный отзыв')

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text