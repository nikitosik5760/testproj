from django import forms
from django.contrib.auth.forms import UserCreationForm


username = forms.CharField(label='Username', max_length=100)
password = forms.CharField(label='Password', max_length=100)
