from typing import Any
from django import forms
from .models import DynamicFieldsModel, JsonFieldDefinition

class DynamicFieldsModelForm(forms.ModelForm):
    class Meta:
        model = DynamicFieldsModel
        exclude = ('dynamic_data',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.foreign_key_id:
            json_fields = instance.foreign_key_id.json_field
            dynamic_data = instance.dynamic_data or {}
            for name, field in json_fields.items():
                field_type = field.get('type')
                initial_value = dynamic_data.get(name, '' if field_type == 'str' else None)
                if field_type == "str":
                    self.fields[name] = forms.CharField(
                        required=False,
                        initial=initial_value,
                        widget=forms.TextInput(attrs={'placeholder': field.get('value', '')})
                    )
                elif field_type == "int":
                    self.fields[name] = forms.IntegerField(
                        required=False,
                        initial=initial_value,
                        widget=forms.NumberInput(attrs={'placeholder': field.get('value', '')})
                    )
                elif field_type == "bool":
                    self.fields[name] = forms.BooleanField(
                        required=False,
                        initial=dynamic_data.get(name, False),
                        widget=forms.CheckboxInput(attrs={'placeholder': field.get('value', '')})
                    )

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, commit=True, *args, **kwargs) -> DynamicFieldsModel:
        instance = super(DynamicFieldsModelForm, self).save(commit=False, *args, **kwargs)
        dynamic_values = {}
        json_fields_id = self.instance.foreign_key_id_id
        json_fields = JsonFieldDefinition.objects.get(id=json_fields_id).json_field
        for name in json_fields.keys():
            if name in self.cleaned_data:
                dynamic_values[name] = self.cleaned_data[name]
        instance.dynamic_data = dynamic_values
        if commit:
            instance.save()
        return instance
