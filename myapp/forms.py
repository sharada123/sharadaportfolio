from django import forms

class ContactForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=100)
    lname = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    mob = forms.CharField(label='Mobile Number', max_length=15)
    msg = forms.CharField(label='Message', widget=forms.Textarea)
