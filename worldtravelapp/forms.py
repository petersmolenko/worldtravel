from django import forms

from .models import Post, UserProfile, Comment, Worker, Message, Tour, NearestDate, Day, Country, City, HotTour
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'city', 'birthday')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'short_descript', 'text', 'tags', 'photo')
		widgets = {
        'title' : forms.TextInput(attrs={'placeholder' : 'Заголовок', 'class' : 'form-control'}),
        'short_descript' : forms.Textarea(attrs={'placeholder' : 'Краткое описание', 'rows' : '7', 'class' : 'form-control'}),
        'text' : forms.Textarea(attrs={'placeholder' : 'Текст статьи', 'rows' : '15', 'class' : 'form-control'}),
        'tags' : forms.TextInput(attrs={'placeholder' : 'тэг1, тэг2, ..', 'class' : 'form-control'}),
        'photo' : forms.FileInput(attrs={'class' : 'custom-file-input', 'lang' : 'ru'}),
    }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('__all__')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')

class ToursForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ('__all__')

class NearestDateForm(forms.ModelForm):
    class Meta:
        model = NearestDate
        fields = ('date', )

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ('number', 'title', 'text')

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('__all__')

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('__all__')

class HotTourForm(forms.ModelForm):
    class Meta:
        model = HotTour
        fields = ('__all__')