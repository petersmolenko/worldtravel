from django import forms

from .models import Post

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