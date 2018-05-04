from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short_descript = models.CharField(max_length=300, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Текст статьи')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    photo_prev = models.ImageField(upload_to='news_images', blank=True, default='', verbose_name='Фото превью')
    photo = models.ImageField(upload_to='news_images', blank=True, default='', verbose_name='Фото к статье')
    tags = models.CharField(max_length=100, verbose_name='Тэги')

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'
        ordering=['created_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
