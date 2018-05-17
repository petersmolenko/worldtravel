from django.contrib import admin
from .models import Post, Comment, NearestDate, Tour, Message, Worker, Day, Review, Country, City, HotTour, Order
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'
   
# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline, )
 

class PostInline(admin.StackedInline):
	model = Comment

class AdminPost(admin.ModelAdmin):
	list_display = ['title', 'created_date']
	inlines = [PostInline]


class DayInline(admin.StackedInline):
    model = Day
    extra=0
    verbose_name_plural = 'Программа тура'

class DateInline(admin.StackedInline):
    model = NearestDate
    extra=0
    verbose_name_plural = 'Ближайшие даты'

class AdminDays(admin.ModelAdmin):
	list_display = ['title', 'type_tour', 'price']
	inlines = [DayInline, DateInline]

class AdminOrder(admin.ModelAdmin):
    list_display = ['order_date', 'tour', 'status']
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, AdminPost)
admin.site.register(Tour, AdminDays)
admin.site.register(Message)
admin.site.register(HotTour)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Review)
admin.site.register(Worker)
admin.site.register(Order, AdminOrder)
