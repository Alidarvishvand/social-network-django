from django import forms


class UserRegisteForm(forms.Form):
    username = forms.CharField()
    email= forms.EmailField()
    password = forms.CharField()