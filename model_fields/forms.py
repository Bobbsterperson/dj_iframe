from django import forms
from .models import AllFieldsModel

class AllFieldsModelForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    file = forms.FileField(required=False)

    class Meta:
        model = AllFieldsModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AllFieldsModelForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.json_data:
            self.fields['name'].initial = self.instance.json_data.get('name', '')
            self.fields['email'].initial = self.instance.json_data.get('email', '')
            self.fields['phone'].initial = self.instance.json_data.get('phone', '')