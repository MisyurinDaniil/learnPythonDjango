# импортируем класс forms
from django import forms

class OrderForm(forms.Form):
    # Создаем два поля класса OrderForm
    # Создаем два input type=text, все поля являеютмя обязательными для заполнения поумолчанию,
    # форма не отправится без заполненных полей, имеет встроенную валидацию
    # required=False - делает поле необязательным
    # widget=forms.TextInput(attrs={'class' : 'css-input'} - зададим класс тегу input для настройки css
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
