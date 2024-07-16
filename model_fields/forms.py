from django import forms
from .models import AllFieldsModel

class AllFieldsModelForm(forms.ModelForm):
    class Meta:
        model = AllFieldsModel
        exclude = ('json_data',)  # Exclude json_data field from form display

    def __init__(self, *args, **kwargs):
        super(AllFieldsModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['name'].initial = self.instance.name
            self.fields['email'].initial = self.instance.email
            self.fields['phone'].initial = self.instance.phone
