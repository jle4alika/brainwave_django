from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'full_name')

    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'ivan123'})
            self.fields['full_name'].widget.attrs.update({"placeholder": 'Иван Иванов'})
            self.fields['email'].widget.attrs.update({"placeholder": 'example@mail.ru'})
            self.fields['password1'].widget.attrs.update({"placeholder": '•••••'})
            self.fields['password2'].widget.attrs.update({"placeholder": '•••••'})

            self.fields['username'].label = 'Логин'
            self.fields['full_name'].label = 'Полное имя'
            self.fields['email'].label = 'Email'
            self.fields['password1'].label = 'Пароль'
            self.fields['password2'].label = 'Повторите пароль'
            
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class UserLoginForm(AuthenticationForm):
    """
    Форма авторизации на сайте
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'Пароль пользователя'
            
            self.fields['username'].label = 'Логин'
            self.fields['password'].label = 'Пароль'
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class UserInfoChangeForm(forms.ModelForm):
    """
    Форма авторизации на сайте
    """
    class Meta:
        model = User
        fields = ('full_name',  'image')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Поле full_name
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Иван Иванов'
        })
        self.fields['full_name'].label = 'Введите новое полное имя'

        # Поле image
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['image'].label = 'Выберите новое фото профиля'
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})