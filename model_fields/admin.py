from django.contrib import admin
from .models import DynamicFieldsModel, JsonFieldDefinition
from .forms import DynamicFieldsModelForm

@admin.register(DynamicFieldsModel)
class DynamicFieldsModelAdmin(admin.ModelAdmin):
    form = DynamicFieldsModelForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

@admin.register(JsonFieldDefinition)
class JsonFieldDefinitionAdmin(admin.ModelAdmin):
    pass