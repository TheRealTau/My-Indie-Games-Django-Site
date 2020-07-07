from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Your name here'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder':'Your email here'}
    ))
    comments = forms.CharField(label="Comments", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5, 'placeholder': "Your comments"}
    ))