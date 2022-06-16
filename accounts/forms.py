from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "phone_number", "password1", "password2")


class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length=50, help_text='Bro parol login yozsez qirasiz ')

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid inputs')


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [ 'f_name', 'l_name', 'sex', 'date_birthday']