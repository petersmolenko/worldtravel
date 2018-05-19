from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='users/', blank=True, verbose_name='Фото профиля')
    city = models.CharField(max_length=30, blank=True, verbose_name='Город')
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
    tel = models.CharField(max_length=30, blank=True, verbose_name='Номер телефона')
 
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
    CONTINENT_CHOICES = (
        ('Африка', 'Африка'),
        ('Азия', 'Азия'),
        ('Австралия', 'Австралия'),
        ('Россия', 'Россия'),
        ('Европа', 'Европа'),
        ('Северная Америка', 'Северная Америка'),
        ('Южная Америка', 'Южная Америка'),
    )
    TYPE_TOUR_CHOICES = (
        ('EXC', 'Экскурсионный'),
        ('BEA', 'Пляжный'),
        ('WEE', 'Выходного дня'),
        ('ACT', 'Активный'),
    )
    TYPE_TRANSPORT_CHOICES = (
        ('AUT', 'Атобусный'),
        ('AVI', 'Авиа'),
        ('CRU', 'Круизный'),
    )
    type_tour = models.CharField(max_length=3, choices=TYPE_TOUR_CHOICES, default='EXC', verbose_name='Тип тура')
    transport = models.CharField(max_length=3, choices=TYPE_TRANSPORT_CHOICES, default='AUT', verbose_name='Тип транспорта')
    duration = models.PositiveSmallIntegerField(verbose_name='Продолжительность')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    citys = models.ManyToManyField('worldtravelapp.City', verbose_name='Города', related_name='tours')
    countrys = models.ManyToManyField('worldtravelapp.Country', related_name='tours', verbose_name='Страны')
    title = models.CharField(max_length=200, verbose_name='Название тура')
    text = models.TextField(verbose_name='Описание тура')
    useful_info = models.TextField(verbose_name='Полезная информация')
    tour_in = models.TextField(verbose_name='Входит в стоимость')
    tour_out = models.TextField(verbose_name='Не входит в стоимость')
    photo = models.ImageField(upload_to='tours_images/', blank=True, default='', verbose_name='Фото тура')
    continent = models.CharField(choices=CONTINENT_CHOICES, default='Россия', max_length=20, verbose_name='Континент')
    discount_tour = models.BooleanField(default=False, verbose_name='Скидка', blank=True)
    complete = models.BooleanField(default=False, verbose_name='Готов', blank=True)
    order_count = models.PositiveSmallIntegerField(verbose_name='Количество заказов', default=0)

    
    class Meta:
        verbose_name='Тур'
        verbose_name_plural='Туры'
        ordering=['title']

    def add_order(self):
        self.order_count+=1
        self.save()


    def discounter(self):
        if self.discount_tour == True:
            self.discount_tour = False
        else:
            self.discount_tour = True
        self.save()

    def is_discount_get(self, htour_date):
        if self.discount_tour == True and str(self.hottour.date_tour) == htour_date:
            return self.price - ((self.price/100)*self.hottour.discount)
        else:
            return self.price

    def discount_get(self):
        if self.discount_tour == True:
            return self.price - ((self.price/100)*self.hottour.discount)
        else:
            return self.price
        
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title


class Day(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок дня')
    number = models.PositiveSmallIntegerField(verbose_name='Номер дня')
    text = models.TextField(verbose_name='Описание дня')
    tours_list = models.ForeignKey('worldtravelapp.Tour', related_name='dates', on_delete=models.CASCADE, verbose_name='Тур')

    class Meta:
        verbose_name='День'
        verbose_name_plural='Дни'
        unique_together = ('number', 'tours_list',)

    def __str__(self):
        return self.title





class NearestDate(models.Model):
    tour = models.ForeignKey('worldtravelapp.Tour', related_name='nearestdates', on_delete=models.CASCADE, verbose_name='Тур')
    date = models.DateField(default=timezone.now, verbose_name='Дата тура', blank=True)
    count_place = models.PositiveSmallIntegerField(verbose_name='Количество мест', blank=True, null=True, default=40)

    class Meta:
        ordering = ['date']
        verbose_name='Дата тура'
        verbose_name_plural='Даты туров'

    def place_count(self):
        if self.count_place > 1:
            self.count_place-=1
            self.save()
        elif self.count_place == 1:
            self.delete()

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
    photo = models.ImageField(upload_to='workers_images/', blank=True, default='', verbose_name='Фото сотрудника')

    class Meta:
        verbose_name='Сотрудник'
        verbose_name_plural='Сотрудники'
        unique_together = ('first_name', 'last_name',)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.last_name


class Country(models.Model):
    CONTINENT_CHOICES = (
        ('Африка', 'Африка'),
        ('Азия', 'Азия'),
        ('Австралия', 'Австралия'),
        ('Россия', 'Россия'),
        ('Европа', 'Европа'),
        ('Северная Америка', 'Северная Америка'),
        ('Южная Америка', 'Южная Америка'),
    )
    title = models.CharField(max_length=30, verbose_name='Название', unique=True)
    continent = models.CharField(choices=CONTINENT_CHOICES, default='Россия', max_length=50, verbose_name='Континент')
    photo = models.ImageField(upload_to='countrys_images/', blank=True, verbose_name='Фото страны')

    class Meta:
        verbose_name='Страна'
        verbose_name_plural='Страны'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название', unique=True)
    country = models.ForeignKey('worldtravelapp.Country', related_name='citys', on_delete=models.CASCADE, verbose_name='Страна')
    photo = models.ImageField(upload_to='citys_images/', blank=True, verbose_name='Фото города')

    class Meta:
        verbose_name='Город'
        verbose_name_plural='Города'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title


class HotTour(models.Model):
    tour = models.OneToOneField('worldtravelapp.Tour', related_name='hottour', on_delete=models.CASCADE, verbose_name='Тур')
    date_tour = models.DateField(default=timezone.now, verbose_name='Дата тура', blank=True)
    text = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='hottours_images/photos/', verbose_name='Фото тура')
    banner = models.ImageField(upload_to='hottours_images/banners/', verbose_name='Баннер тура')
    discount = models.PositiveSmallIntegerField(verbose_name='Скидка')
    advertise = models.BooleanField(default=False, verbose_name='Реклама')
    class Meta:
        verbose_name='Горящий тур'
        verbose_name_plural='Горящие туры'

    def __str__(self):
        return self.tour.title




class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    tour = models.ForeignKey('worldtravelapp.Tour', related_name='reviews', on_delete=models.CASCADE, verbose_name='Тур')
    text = models.TextField(verbose_name='Отзыв')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    approved_review = models.BooleanField(default=False, verbose_name='Одобренный отзыв')

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.text

class Order(models.Model):
    client = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Заказчик')
    tour = models.ForeignKey('worldtravelapp.Tour', related_name='orders', on_delete=models.CASCADE, verbose_name='Тур')
    price = models.PositiveSmallIntegerField(verbose_name='Сумма')
    tour_date = models.DateField(default=timezone.now, verbose_name='Дата тура', blank=True)
    order_date = models.DateTimeField(default=timezone.now, verbose_name='Время заказа')
    desire_order = models.BooleanField(default=False, verbose_name='Желаемый заказ')
    order = models.BooleanField(default=False, verbose_name='Заказанный')
    order_complete = models.BooleanField(default=False, verbose_name='Обаботанный заказ')
    status = models.CharField(max_length=20, verbose_name='Статус', blank=True)

    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='Заказы'

    def desire(self):
        self.desire_order= True
        self.save()

    def order_get(self):
        self.desire_order= False
        self.order= True
        self.save()

    def complete(self):
        self.order= False
        self.order_complete= True
        self.save()

    def __str__(self):
        return str(self.pk)