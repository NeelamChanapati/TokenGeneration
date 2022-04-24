from django import forms
from .models import token
  
class detailsForm(forms.ModelForm):
    class Meta:
        model = token
        fields = ['name', 'ph_no', 'item']