from django import forms

class SignInForms(forms.Form):
    username = forms.CharField(max_length=40,label="Username")
    password = forms.PasswordInput(label='Password')
