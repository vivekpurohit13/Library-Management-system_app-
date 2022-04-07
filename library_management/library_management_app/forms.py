from dataclasses import fields
from pyexpat import model
from django import forms
from .models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model=BookModel
        fields=('__all__')