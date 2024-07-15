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
        'name',
        'email',
        'phone',
        'file',
    )
    search_fields = ('char_field', 'text_field', 'email_field', 'name', 'email', 'phone')
    list_filter = ('bool_field', 'date_field', 'datetime_field')

    fieldsets = (
        (None, {
            'fields': (
                'char_field', 'bool_field', 'int_field', 'float_field', 'decimal_field',
                'date_field', 'datetime_field', 'email_field', 'url_field', 'uuid_field',
            )
        }),
        ('JSON Data', {
            'fields': ('name', 'email', 'phone', 'file')
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.name = form.cleaned_data.get('name', '')
        obj.email = form.cleaned_data.get('email', '')
        obj.phone = form.cleaned_data.get('phone', '')
        obj.file = request.FILES.get('file', None)
        
        super().save_model(request, obj, form, change)
