from django.contrib import admin
from .models import AllFieldsModel
from .forms import AllFieldsModelForm

@admin.register(AllFieldsModel)
class AllFieldsModelAdmin(admin.ModelAdmin):
    form = AllFieldsModelForm
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
        'uuid_field',
        'display_json_name',
        'display_json_email',
        'display_json_phone',
        'display_json_file',
    )
    search_fields = ('char_field', 'text_field', 'email_field')
    list_filter = ('bool_field', 'date_field', 'datetime_field')

    fieldsets = (
        (None, {
            'fields': ('char_field', 'bool_field', 'int_field', 'float_field', 'decimal_field', 'date_field', 'datetime_field', 'email_field', 'url_field', 'uuid_field', 'text_field')
        }),
        ('JSON Data', {
            'fields': ('name', 'email', 'phone', 'file')
        }),
    )

    def display_json_name(self, obj):
        return obj.json_data.get('name', '')
    display_json_name.short_description = 'Name'

    def display_json_email(self, obj):
        return obj.json_data.get('email', '')
    display_json_email.short_description = 'Email'

    def display_json_phone(self, obj):
        return obj.json_data.get('phone', '')
    display_json_phone.short_description = 'Phone'

    def display_json_file(self, obj):
        return obj.json_data.get('file', '')
    display_json_file.short_description = 'File'

    def save_model(self, request, obj, form, change):
        obj.json_data = {
            'name': form.cleaned_data.get('name', ''),
            'email': form.cleaned_data.get('email', ''),
            'phone': form.cleaned_data.get('phone', ''),
        }
        
        if 'file' in request.FILES:
            obj.json_data['file'] = request.FILES['file'].name

        super().save_model(request, obj, form, change)