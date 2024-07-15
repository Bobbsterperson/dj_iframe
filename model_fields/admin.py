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

    def save_model(self, request, obj, form, change):
        obj.char_field = form.cleaned_data['char_field']
        obj.bool_field = form.cleaned_data['bool_field']
        obj.int_field = form.cleaned_data['int_field']
        obj.float_field = form.cleaned_data['float_field']
        obj.decimal_field = form.cleaned_data['decimal_field']
        obj.date_field = form.cleaned_data['date_field']
        obj.datetime_field = form.cleaned_data['datetime_field']
        obj.email_field = form.cleaned_data['email_field']
        obj.url_field = form.cleaned_data['url_field']
        obj.uuid_field = form.cleaned_data['uuid_field']
        obj.html = form.cleaned_data['html']
        obj.css = form.cleaned_data['css']
        obj.js = form.cleaned_data['js']

        super().save_model(request, obj, form, change)
