from django import forms
from .models import libros

class LibrosForm(forms.ModelForm):
    class Meta:
        model = libros
        fields ='__all__'




