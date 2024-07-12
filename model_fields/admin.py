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
        'datetime_field',
        'email_field',
        'url_field',
        'uuid_field'
    )
    search_fields = ('char_field', 'text_field', 'email_field')
    list_filter = ('bool_field', 'date_field', 'datetime_field')
