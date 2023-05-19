from django import forms
from django.core.exceptions import ValidationError
from .models import *


class ArticlesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not field == 'is_published':
                self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['cat'].empty_label = 'Категория не выбрана'
        self.fields['is_published'].label = 'Опубликовать:  '
        self.fields['title'].widget.attrs['placeholder'] = 'Заголовок'
        self.fields['anons'].widget.attrs['placeholder'] = 'Анонс'
        self.fields['full_text'].widget.attrs['placeholder'] = 'Описание'
        self.fields['cat'].widget.attrs['placeholder'] = 'Категория: '

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Слишком много символов!')

        if len(Articles.objects.filter(title=title)) != 0:
            raise ValidationError('Форма с таким заголовком уже существует!')

        return title

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'is_published', 'cat']


