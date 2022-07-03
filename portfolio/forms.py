from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'text')

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    company = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea)
