from django_registration.forms import RegistrationForm
from .models import User, ShoppingList, Product
from django import forms


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User


class AddBuy(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = []


class ChangeWarranty(forms.ModelForm):
    class Meta:
        model = Product
        fields = []


class ChangeUserInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'region', 'city', 'address', 'delivery']



