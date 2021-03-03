from django import forms

class urlmanipulate(forms.Form):
    originalurl=forms.URLField()
    shorturl=forms.URLField()