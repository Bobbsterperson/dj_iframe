from django.contrib import admin
from .models import DynamicFieldsModel, JsonFieldDefinition
from .forms import DynamicFieldsModelForm

@admin.register(DynamicFieldsModel)
class DynamicFieldsModelAdmin(admin.ModelAdmin):
    """
    Admin interface for DynamicFieldsModel, which includes dynamically generated fields.
    """
    form = DynamicFieldsModelForm

    def get_fieldsets(self, request, obj=None):
        """
        Dynamically generate fieldsets based on JSON field definitions.
        """
        json_generator = JsonFieldDefinition.objects.first()
        json_data = json_generator.json_dt if json_generator else {}
        all_field_names = [f.name for f in DynamicFieldsModel._meta.get_fields()]
        json_fields = []
        for key in json_data.keys():
            if key in all_field_names:
                json_fields.append(key)
        fieldsets = tuple(json_fields)
        return fieldsets

    def save_model(self, request, obj, form, change):
        """
        Override save_model to update json_data with dynamic fields before saving.
        """
        fieldsets = self.get_fieldsets(request)
        json_data_fields = []
        for fieldset in fieldsets:
            if fieldset[0] == 'JSON Data':
                json_data_fields.extend(fieldset[1]['fields'])
        obj.update_json_data(json_data_fields)
        super().save_model(request, obj, form, change)

@admin.register(JsonFieldDefinition)
class JsonFieldDefinitionAdmin(admin.ModelAdmin):
    """
    Admin interface for JsonFieldDefinition.
    """
    pass
