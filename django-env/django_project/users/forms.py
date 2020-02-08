from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() ## required=True is default
    
    class Meta:
        model = User ## Use the default User model. When save, save to User model
        fields = ['username', 'email', 'password1', 'password2'] ## These are going to be shown on our form, in THIS order.

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']