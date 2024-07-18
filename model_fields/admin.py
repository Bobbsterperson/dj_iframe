from django.contrib import admin
from .models import AllFieldsModel

@admin.register(AllFieldsModel)
class AllFieldsModelAdmin(admin.ModelAdmin):
    list_display = (
        'char_field',
        'bool_field',
        'int_field',
        'float_field',
        'decimal_field',
        'date_field',
        'uuid_field',
    )
    search_fields = ('char_field', 'text_field', 'name', 'email', 'phone')
    list_filter = ('bool_field', 'date_field')

    fieldsets = (
        (None, {
            'fields': (
                'char_field', 'bool_field', 'int_field', 'float_field', 'decimal_field',
                'date_field', 'uuid_field',
            )
        }),
        ('JSON Data', {
            'fields': ('name', 'email', 'phone', 'file', "twowordpoem", 'url_field', "datetime_field")
        }),
    )

    def save_model(self, request, obj, form, change):
        for key in obj.json_data.keys():
            setattr(obj, key, form.cleaned_data.get(key))
        super().save_model(request, obj, form, change)
