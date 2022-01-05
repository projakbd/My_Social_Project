from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'margin-top:20px'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password', 'style': 'margin-top:20px'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'style': 'margin-top:20px'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', )

class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date',}))
    class Meta:
        model = UserProfile()
        exclude = ('user', )
