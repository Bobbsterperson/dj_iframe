from django import forms
from .models import DynamicFieldsModel, JsonFieldDefinition

class DynamicFieldsModelForm(forms.ModelForm):
    """
    Form to dynamically create fields based on JSON field definitions.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        json_generator = JsonFieldDefinition.objects.first()
        json_data = json_generator.json_dt if json_generator else {}
        for key, value in json_data.items():
            if key not in [f.name for f in DynamicFieldsModel._meta.get_fields()]:
                form_type = {
                    'str': forms.CharField,
                    'int': forms.IntegerField,
                    'float': forms.FloatField,
                    'bool': forms.BooleanField,
                    'date': forms.DateField,
                    'datetime': forms.DateTimeField,
                    'decimal': forms.DecimalField,
                }.get(value['type'], forms.CharField)
                self.fields[key] = form_type(
                    label=key.capitalize(),
                    initial=value['value'],
                    required=False
                )

    class Meta:
        model = DynamicFieldsModel
        exclude = ('json_data',)
