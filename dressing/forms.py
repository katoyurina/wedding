from tkinter.tix import Select
from unicodedata import category
from django import forms
from django.shortcuts import render
from .models import Select


class SelectForm(forms.ModelForm):
    class Meta:
        model = Select
        fields = ["name","categoly_Choice","num_Choice"]        
        widgets = {'name': forms.HiddenInput(), 'categoly_Choice': forms.HiddenInput(), 'num_Choice': forms.HiddenInput()}
    

