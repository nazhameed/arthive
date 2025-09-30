from django import forms
from django.contrib.auth.models import User
from .models import Child

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age']
        # Add Bootstrap classes for better UI
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }
