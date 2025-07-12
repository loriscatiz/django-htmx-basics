from django import forms
from core.models import State, Country

class MyForm(forms.Form):
    country = forms.ModelChoiceField(queryset=None, widget=forms.Select())
    state = forms.ModelChoiceField(queryset=None, widget=forms.Select())
    city = forms.ModelChoiceField(queryset=None, widget=forms.Select())
    
        
