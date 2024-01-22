from django import forms


class UserRegisteForm(forms.Form):
    username = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'your-mail@gmial.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))