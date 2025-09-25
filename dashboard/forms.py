from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from products.models import Product
from orders.models import Order


# --- Custom User Signup Form ---
# Extends Django's UserCreationForm and adds extra fields (first name, last name, email)
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


# --- Product Form ---
# Used to create or update a product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", "description", "price", "stock", 
            "category", "brand", "weight", "is_active", "image"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "price": forms.NumberInput(attrs={"min": "0", "step": "0.01", "class": "form-control"}),
            "stock": forms.NumberInput(attrs={"min": "0", "class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"min": "0", "step": "0.01", "class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control", "accept": "image/*"}),
        }


# --- Order Form ---
# Minimal form for updating the order status
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["status"]


# --- User Profile Update Form ---
# Used to update user profile information
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }


# --- Custom Password Change Form ---
# Extends Django's PasswordChangeForm and customizes the input styling
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap-like styling to password fields
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control rounded-pill shadow-sm',
            'required': True
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control rounded-pill shadow-sm',
            'required': True
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control rounded-pill shadow-sm',
            'required': True
        })
