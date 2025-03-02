from django import forms
from .models import *

class UrlCreationForm(forms.ModelForm):
    class Meta:
        model = ShortenUrl
        fields = ["url"]

class UrlUpdateForm(forms.ModelForm):
    class Meta:
        model = ShortenUrl
        fields = ["url"]

class UrlStatsForm(forms.ModelForm):
    class Meta:
        model = ShortenUrl
        fields = "__all__"