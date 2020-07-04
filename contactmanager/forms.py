from django import forms
from contactmanager.models import Contact


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'mobile', 'fax', 'image')
        