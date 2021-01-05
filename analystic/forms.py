from django import forms
from django.forms import DateField, IntegerField
from .models import *




class DataInputForm(forms.ModelForm):
    class Meta:
        model = DataEntery
        fields = ['infected','infectedDate']
    
    infected = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    infectedDate = forms.DateField(widget = forms.SelectDateWidget(attrs={'class':'form-control'}))