from django import forms
from .models import Snippet, Group

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['body']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

