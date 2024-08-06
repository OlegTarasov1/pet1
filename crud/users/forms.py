from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label = '', widget=forms.TextInput(attrs = {'placeholder': 'username or email'}))
    password = forms.CharField(label = '', widget=forms.PasswordInput(attrs = {'placeholder': 'password'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label = '', widget = forms.TextInput(attrs = {'placeholder': 'username'}))
    password1 = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'password'}))
    password2 = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'password again'}))
    email = forms.CharField(label = '', widget = forms.EmailInput(attrs = {'placeholder': 'email'}))
    first_name = forms.CharField(label = '', widget = forms.TextInput(attrs = {'placeholder': 'first name'}))
    last_name = forms.CharField(label = '', widget = forms.TextInput(attrs = {'placeholder': 'last name'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match!")
        return cd['password1']
    
    def clean_email(self):
        email = self.cleaned_data['email'] 
        if get_user_model().objects.filter(email = email).exists():
            raise forms.ValidationError('This email has already been registered!')
        return email
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'old password'}))
    new_password1 = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'new password'}))
    new_password2 = forms.CharField(label = '', widget = forms.PasswordInput(attrs = {'placeholder': 'new password again'}))