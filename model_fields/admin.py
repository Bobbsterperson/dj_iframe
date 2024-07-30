from django.contrib import admin
from .models import DynamicFieldsModel, JsonFieldDefinition
from .forms import DynamicFieldsModelForm

@admin.register(DynamicFieldsModel)
class DynamicFieldsModelAdmin(admin.ModelAdmin):
    form = DynamicFieldsModelForm

    def get_fieldsets(self, request, obj=None):
        """
        Dynamically generate fieldsets based on JSON field definitions.
        """
        json_generator = JsonFieldDefinition.objects.first()
        json_data = json_generator.json_dt if json_generator else {}
        json_fields = [key for key in json_data.keys()]
        fieldsets = (
            (None, {
                'fields': ('char_field', 'int_field', 'float_field', 'date_field', *json_fields)
            }),
        )
        return fieldsets

    def save_model(self, request, obj, form, change):
        """
        Override save_model to update json_data with dynamic fields before saving.
        """
        json_data_fields = self.get_json_fields()
        obj.update_json_data(json_data_fields)
        super().save_model(request, obj, form, change)

    def get_json_fields(self):
        """
        Get JSON-defined fields.
        """
        json_generator = JsonFieldDefinition.objects.first()
        return json_generator.json_dt.keys() if json_generator else []

@admin.register(JsonFieldDefinition)
class JsonFieldDefinitionAdmin(admin.ModelAdmin):
    pass
