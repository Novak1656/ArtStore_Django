from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.forms import CharField, EmailInput, PasswordInput, EmailField,\
    TextInput, BooleanField, CheckboxInput, TypedChoiceField, Select


class UserRegisterForm(UserCreationForm):
    username = CharField(label='Логин',
                               widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(label='E-mail',
                             widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Пароль',
                                widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='Подтверждение пароля',
                                widget=PasswordInput(attrs={'class': 'form-control'}))

    roles = TypedChoiceField(label='Я', empty_value=('Пользователь', 'Пользователь (может покупать иллюстрации)'),
                             choices=(('Пользователь', 'Пользователь (может покупать иллюстрации)'),
                                      ('Автор', 'Автор (может покупать иллюстрации, а также продавать свои)')),
                             widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'roles')


class UserLoginForm(AuthenticationForm):
    username = CharField(label='Логин',
                               widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Пароль',
                               widget=PasswordInput(attrs={'class': 'form-control'}))
    remember_me = BooleanField(label='Запомнить меня', required=False)
