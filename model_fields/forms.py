from django import forms
from .models import DynamicFieldsModel, JsonFieldDefinition


class DynamicFieldsModelForm(forms.ModelForm):
    bool_field = forms.BooleanField(label='Boolean field', initial=False, required=False)

