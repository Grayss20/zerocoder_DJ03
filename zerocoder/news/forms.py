from .models import NewsPost
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class NewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }
