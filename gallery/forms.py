from django import forms
from django.contrib.auth.models import User
from .models import Child, Artwork

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

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['image', 'title', 'description', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['created_at'].required = False
