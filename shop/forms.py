from django.forms import ModelForm

from .models import Product
from django.contrib.auth.models import User


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'price')

        labels = {'name': 'Name', 'category': 'Category', 'price': 'Price'}


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

        labels = {'username': 'Username', 'email': 'Email'}
