from django import forms


class UserForm(forms.Form):
    login = forms.CharField(label="Логин", help_text="Имя пользователя или адрес электронной почты")
    password = forms.CharField(label="Пароль", help_text="Пароль")