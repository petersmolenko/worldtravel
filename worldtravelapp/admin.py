from django.contrib import admin
from .models import Post, Comment
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
	extra = 1

class AdminPost(admin.ModelAdmin):
	list_display = ['title', 'created_date']
	inlines = [PostInline]
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, AdminPost)