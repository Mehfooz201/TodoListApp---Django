from django import forms
from django.forms import TextInput

class TodoForm(forms.Form):
    text = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter todo e.g. Delete junk files', 'arial-label':'Todo', 'aria-describedby':'add-btn'}))
