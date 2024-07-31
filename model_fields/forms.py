from typing import Any
from django import forms
from .models import JsonFieldDefinition, DynamicFieldsModel

class DynamicFieldsModelForm(forms.ModelForm):
    class Meta:
        model = DynamicFieldsModel
        fields = '__all__'
        exclude = []

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.foreign_key_id:
            json_fields = instance.foreign_key_id.json_field
            for name, field in json_fields.items():
                if field['type'] == "str":
                    self.fields[name] = forms.CharField(
                        widget=forms.TextInput(attrs={'placeholder': field['value']}))
                elif field['type'] == "int":
                    self.fields[name] = forms.IntegerField(
                        widget=forms.NumberInput(attrs={'placeholder': field['value']}))
                


    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        return cleaned_data
