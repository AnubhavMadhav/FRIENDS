# map_app/forms.py
from django import forms

class LocationForm(forms.Form):
    name = forms.CharField(max_length=100)
    latitude = forms.FloatField()
    longitude = forms.FloatField()