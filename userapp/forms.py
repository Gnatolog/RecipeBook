from django import forms
from django.contrib.auth.models import User


class UserForms(forms.ModelForm):
    username = forms.CharField(label="Логин пользователя", widget=forms.TextInput
    (attrs={'placeholder': 'Введите логин'}))

    first_name = forms.CharField(label="Имя пользователя", widget=forms.TextInput
    (attrs={'placeholder': 'Введите имя пользователя'}))

    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'user@mail.ru'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Такой email уже существует')
        return data
