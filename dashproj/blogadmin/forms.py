from django import forms

class BlogForm(forms.ModelForm):
    title = forms.CharField(label="Title",max_length=999)