from django import forms
from .models import*


class UserRegistrationForm(forms.ModelForm):
    login = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(min_length=8, label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(min_length=8, label='Повторите пароль', widget=forms.PasswordInput())
    email = forms.CharField(label='E-Mail', widget=forms.EmailInput())
    # BirthDate = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget())
    # About = forms.CharField(label='О себе', required=False, widget=forms.Textarea())
    # Photo = forms.ImageField(label='Аватар', required=False, widget=forms.FileInput())

    class Meta:
        model = Users
        field_order = ['login', 'password', 'password2', 'name','email']
        fields = ['login', 'password', 'password2', 'name', 'email']# обязательно fields | exclude при работе с формой
# class RegisterUserForm(forms.ModelForm):
#     field_order = ['login', 'password', 'password2']
#     class Meta:
#         model = Users
#         exclude = ["is_blocked"]
#         labels = {'login': 'Логин', 'email': 'E-mail', 'name': 'Имя',
#         'address': 'Адрес', 'telephone': 'Телефон',
#         }
#     password = forms.CharField(
#     max_length=24,
#     label = 'Введите пароль',
#     widget = forms.PasswordInput(
#             attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your password'
#             }
#         ),
#     )
#     password2 = forms.CharField(
#     max_length=24,
#     label = 'Подтвердите пароль',
#     widget = forms.PasswordInput(
#             attrs={
#             'class': 'form-control',
#             'placeholder': 'Repeat your password'
#             }
#     ),
#     help_text=("Enter the same password as before, for verification."),
#     )
#
#
# class UserPhoto:
#     pass
#
#
# class RegisterUserPhotoForm(forms.ModelForm):
#     class Meta:
#         model = UserPhoto
#         fields = ['photo']
#         exclude = ['user', 'status']
#         labels = {
#         'photo': 'Фотография',
#     }
