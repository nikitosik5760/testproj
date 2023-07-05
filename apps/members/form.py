from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-contol'})
        self.fields['email'].widget.attrs.update({'class': 'form-contol'})
        self.fields['password1'].widget.attrs.update({'class': 'form-contol'})
        self.fields['password2'].widget.attrs.update({'class': 'form-contol'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(
        attrs={type: 'hidden'}), required=False)

    class Meta:
        model = User
        fields = {'username', 'email',
                  'first_name', 'last_name'}
        widgets = {
            'username': forms.TextInput({'class': 'form-contol'}),
            'email': forms.TextInput({'class': 'form-contol'}),
            'first_name': forms.TextInput({'class': 'form-contol'}),
            'second_name': forms.TextInput({'class': 'form-contol'}),

        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
