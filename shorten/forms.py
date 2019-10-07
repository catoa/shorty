from django import forms
from .models import ShortenedUrl


class ShortenedUrlModelForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ['url', ]
