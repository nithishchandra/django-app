from django import forms

class formExample(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()