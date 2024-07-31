from typing import Any
from django import forms
from .models import DynamicFieldsModel, JsonFieldDefinition

class DynamicFieldsModelForm(forms.ModelForm):
    # dynamic_data = forms.JSONField()  # widget=forms.HiddenInput()
    
    class Meta:
        exclude = ('dynamic_data',)
        model = DynamicFieldsModel
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(DynamicFieldsModelForm, self).__init__(*args, **kwargs)
        
        instance = kwargs.get('instance')
        if instance and instance.foreign_key_id:
            json_fields = instance.foreign_key_id.json_field
            for name, field in json_fields.items():
                if field['type'] == "str":
                    self.fields[name] = forms.CharField(
                        required=False,
                        widget=forms.TextInput(attrs={'placeholder': field['value']}))
                elif field['type'] == "int":
                    self.fields[name] = forms.IntegerField(
                        required=False,
                        widget=forms.NumberInput(attrs={'placeholder': field['value']}))
                elif field['type'] == "bool":
                    self.fields[name] = forms.BooleanField(
                        required=False,
                        widget=forms.CheckboxInput(attrs={'placeholder': field['value']}))


    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, *args, **kwargs) -> DynamicFieldsModel:
        dynamic_values = {}
        json_fields_id = self["foreign_key_id"].value()
        json_fields = JsonFieldDefinition.objects.get(id=json_fields_id).json_field
        
        for name in json_fields.keys():
            dynamic_values[name] = self.cleaned_data.get(name)

        print(dynamic_values)
        
        instance = super(DynamicFieldsModelForm, self).save(*args, **kwargs)
        instance.dynamic_data = dynamic_values
        return instance