from django.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Contacts
from django.core.exceptions import ValidationError
from .tests import valid_number


class ContactsForm(ModelForm):
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not valid_number(phone_number):
            raise ValidationError('Не корректный номер телефона!')
        return phone_number

    def clean_password(self):
        password = self.cleaned_data['password']
        if password != 'begugla123':
            raise ValidationError('Неправильный пароль!')
        return password

    class Meta:
        model = Contacts
        fields = ['title', 'description', 'phone_number', 'password']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя сотрудника'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер сотрудника'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код'
            })
        }


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['email'].widget.attrs['placeholder'] = 'Email (не обязательно)'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'


class FeedbackForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['captcha'].widget.attrs['placeholder'] = 'Пройдите captcha'

    name = CharField(max_length=100)
    email = EmailField()
    content = CharField(widget=Textarea(attrs={'placeholder': 'Описание', 'rows': 7}))
    captcha = CaptchaField()
