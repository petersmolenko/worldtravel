from django import forms

from .models import Post, UserProfile, Comment, Worker, Message, Tour, NearestDate, Day, Country, City, HotTour, Review, Order
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'city', 'birthday', 'tel')
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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
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
        exclude = ('complete', 'discount_tour', 'price_current')

class NearestDateForm(forms.ModelForm):
    class Meta:
        model = NearestDate
        fields = ('date', 'count_place' )

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
        exclude = ('date_tour',)

class SortTourForm(forms.Form):
    sort_tour_choice = (
        ('title', 'По алфавиту'),
        ('price_current', 'По цене &#9650;'),
        ('-price_current', 'По цене &#9660;'),
        ('order_count', 'По популярности &#9650;'),
        ('-order_count', 'По популярности &#9660;'),
    )
    filter_tour_choice = (
        ('', 'Все'),
        ('EXC', 'Экскурсионный'),
        ('BEA', 'Пляжный'),
        ('WEE', 'Выходного дня'),
        ('ACT', 'Активный'),
    )
    type_transport_choice = (
        ('', 'Все'),
        ('AUT', 'Атобусный'),
        ('AVI', 'Авиа'),
        ('CRU', 'Круизный'),
    )
    ordering = forms.ChoiceField(choices = sort_tour_choice, required=False)
    filter_tour = forms.ChoiceField(choices = filter_tour_choice, required=False)
    transport = forms.ChoiceField(choices = type_transport_choice, required=False)
    country = forms.CharField(max_length=20, required=False)
    city = forms.CharField(max_length=20, required=False)
    price_for = forms.FloatField(required=False, min_value=0)
    price_to = forms.FloatField(required=False, min_value=0)
    date_for = forms.CharField(max_length=10, required=False)
    date_to = forms.CharField(max_length=10, required=False)
    inday = forms.IntegerField(required=False, min_value=0)
    outday = forms.IntegerField(required=False, min_value=0)
    hottour = forms.BooleanField(required=False)

class waypointForm(forms.Form):
    def __init__(self, coices, *args, **kwargs):
        super(waypointForm, self).__init__(*args, **kwargs)
        self.fields['waypoints'] = forms.ChoiceField(
            choices=[(o.date, str(o)) for o in coices]
            )