from django import forms
from .models import AllFieldsModel

class AllFieldsModelForm(forms.ModelForm):
    class Meta:
        model = AllFieldsModel
        exclude = ('json_data',)

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if not name:
            raise forms.ValidationError("Name cannot be empty.")
        name_parts = name.split()
        if len(name_parts) < 2:
            raise forms.ValidationError("Please provide both first and last name.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if not email:
            raise forms.ValidationError("Email cannot be empty.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        if not phone:
            raise forms.ValidationError("Phone cannot be empty.")
        return phone

    def clean_file(self):
        file = self.cleaned_data.get('file', None)
        return file

    def __init__(self, *args, **kwargs):
        super(AllFieldsModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].initial = self.instance.name
            self.fields['email'].initial = self.instance.email
            self.fields['phone'].initial = self.instance.phone
