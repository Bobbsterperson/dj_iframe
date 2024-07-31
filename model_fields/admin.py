from django.contrib import admin
from .models import DynamicFieldsModel, JsonFieldDefinition
from .forms import DynamicFieldsModelForm

@admin.register(DynamicFieldsModel)
class DynamicFieldsModelAdmin(admin.ModelAdmin):
    # form = DynamicFieldsModelForm

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            dynamic_keys = obj.foreign_key_id.json_field.keys()
            for key in dynamic_keys:
                fieldsets[0][1]['fields'].append(key)
        return fieldsets
    
    def get_form(self, request, obj=None, change=False, **kwargs):
        return DynamicFieldsModelForm
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(JsonFieldDefinition)
class JsonFieldDefinitionAdmin(admin.ModelAdmin):
    pass
