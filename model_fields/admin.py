from django.contrib import admin
from .models import AllFieldsModel, JsonGenerator
from .forms import AllFieldsModelForm

@admin.register(AllFieldsModel)
class AllFieldsModelAdmin(admin.ModelAdmin):
    form = AllFieldsModelForm

    def get_fieldsets(self, request, obj=None):
        json_generator = JsonGenerator.objects.first()
        json_data = json_generator.json_dt if json_generator else {}

        all_field_names = [f.name for f in AllFieldsModel._meta.get_fields()]
        json_fields = []
        for key in json_data.keys():
            if key in all_field_names:
                json_fields.append(key)

        fieldsets = tuple(json_fields)
        
        return fieldsets

    def save_model(self, request, obj, form, change):
        json_data_fields = [field for fieldset in self.get_fieldsets(request) if fieldset[0] == 'JSON Data' for field in fieldset[1]['fields']]
        obj.update_json_data(json_data_fields)
        super().save_model(request, obj, form, change)


@admin.register(JsonGenerator)
class JsonGeneratorAdmin(admin.ModelAdmin):
    pass