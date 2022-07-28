from django import forms
from authentication.models import User
from django.core.exceptions import ValidationError


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth',)
        widgets = {
            'first_name': forms.TextInput(attrs={"placeholder": "Введите ваше имя...",
                                                 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={"placeholder": "Введите вашу фамилию...",
                                                'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={"placeholder": "Введите вашу дату рождения...",
                                                    'class': 'form-control'}),
        }


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar',)
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }


class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={"placeholder": "Введите адрес электронной почты...",
                                             'class': 'form-control'})
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": "Введите новый логин...",
                                               'class': 'form-control'})
        }


# class PasswordForm(forms.Form):
#     password = forms.CharField(label='Текущий пароль', min_length=8,
#                                widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль...",
#                                                                  'class': 'form-control'}))
#     password_new_1 = forms.CharField(label='Новый пароль', min_length=8,
#                                      widget=forms.PasswordInput(attrs={"placeholder": "Введите новый пароль...",
#                                                                        'class': 'form-control'}))
#     password_new_2 = forms.CharField(label='Подтверждение пароля', min_length=8,
#                                      widget=forms.PasswordInput(attrs={"placeholder": "Введите новый пароль ещё раз...",
#                                                                        "class": "form-control"}))
#
#     def password_chek(self):
#         p1 = self.cleaned_data['password_new_1']
#         p2 = self.cleaned_data['password_new_2']
#         if p1 != p2:
#             raise ValidationError('Пароли не совпадают')
#         return True
