from django.shortcuts import render
from .models import ComplaintAndSuggestion
from django import forms

class ComplaintAndSuggestionForm(forms.ModelForm):
    class Meta:
        model = ComplaintAndSuggestion
        fields = ['name', 'complaint']