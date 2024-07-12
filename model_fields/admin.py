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

    def save_model(self, request, obj, form, change):
        obj.json_data = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'phone': form.cleaned_data['phone'],
        }
        
        if 'file' in request.FILES:
            obj.json_data['file'] = request.FILES['file'].name

        super().save_model(request, obj, form, change)
