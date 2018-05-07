from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users', blank=True, verbose_name='Фото профиля')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
 
    def __unicode__(self):
        return self.user
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

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
        
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title
