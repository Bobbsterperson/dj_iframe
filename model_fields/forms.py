from django import forms
from .models import AllFieldsModel
import json

class AllFieldsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and isinstance(instance.json_data, dict):
            json_data = instance.json_data
            
            for key, value in json_data.items():
                if key == 'file':
                    form_type = forms.FileField
                else:
                    form_type = forms.CharField
                self.fields[key] = form_type(label=key.capitalize(), initial=value)

    class Meta:
        model = AllFieldsModel
        exclude = ('json_data',)
