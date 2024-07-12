from django import forms
from .models import AllFieldsModel

class AllFieldsModelForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=15, required=False)
    file = forms.FileField(required=False)

    class Meta:
        model = AllFieldsModel
        fields = '__all__'
