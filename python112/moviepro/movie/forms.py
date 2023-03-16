from django import forms
from .models import ko


class movieform(forms.ModelForm):
    class Meta:
        model = ko
        fields = ['name', 'year', 'des', 'image']
