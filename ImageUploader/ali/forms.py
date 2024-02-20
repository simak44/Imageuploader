from .models import myimage
from django import forms

class imageform(forms.ModelForm):
    class Meta:
        model = myimage
        fields = '__all__'
        labels = {'photo':''}