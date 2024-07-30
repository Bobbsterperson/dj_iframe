from django import forms
from .models import AllFieldsModel

class AllFieldsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and isinstance(instance.json_data, dict):
            json_data = instance.json_data
            for key, value in json_data.items():
                if key in [f.name for f in AllFieldsModel._meta.get_fields()]:
                    if value['type'] == 'str':
                        form_type = forms.CharField
                    elif value['type'] == 'int':
                        form_type = forms.IntegerField
                    else:
                        form_type = forms.CharField
                    self.fields[key] = form_type(label=key.capitalize(), initial=value['value'])

    class Meta:
        model = AllFieldsModel
        exclude = ('json_data',)
