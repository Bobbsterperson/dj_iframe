from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date, time
from decimal import Decimal

class DynamicFieldsModel(models.Model):
    """
    Model to store various fields, including dynamically generated fields from JSON data.
    """

    bool_field = models.BooleanField(default=False)
    # json_data = models.JSONField(default=dict)
    # null_bool_field = models.BooleanField(null=True, blank=True)
    # char_field = models.CharField(max_length=100, null=True, blank=True)
    # text_field = RichTextField(blank=True, null=True)
    # int_field = models.IntegerField(null=True, blank=True)
    # float_field = models.FloatField(null=True, blank=True)
    # decimal_field = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # date_field = models.DateField(null=True, blank=True)
    # time_field = models.TimeField(null=True, blank=True)
    # url_field = models.URLField(null=True, blank=True)
    # uuid_field = models.UUIDField(null=True, blank=True)
    # name = models.CharField(max_length=100, blank=True, default='')
    # email = models.EmailField(blank=True, default='')
    # phone = models.CharField(max_length=15, blank=True, default='')
    # file = models.FileField(upload_to='files/', null=True, blank=True)
    # datetime_field = models.DateTimeField(null=True, blank=True)
    # bingo = models.CharField(max_length=100, blank=True, default='')

    def update_json_data(self, fields):
        """
        Update the json_data field with values from the specified fields.
        """
        self.json_data = {}
        for field in fields:
            value = getattr(self, field)
            if isinstance(value, models.fields.files.FieldFile):
                if value:
                    file_name = value.name.split('/')[-1]
                    file_path = value.url
                    self.json_data[field] = {'name': file_name, 'path': file_path}
                else:
                    self.json_data[field] = {'name': '', 'path': ''}
            elif isinstance(value, (datetime, date, time)):
                self.json_data[field] = value.isoformat() if value else None
            elif isinstance(value, Decimal):
                self.json_data[field] = str(value)
            elif isinstance(value, bool):
                self.json_data[field] = value
            else:
                self.json_data[field] = str(value)

    def save(self, *args, **kwargs):
        """
        Override save method to update json_data with dynamic fields.
        """
        json_data_fields = self.get_dynamic_fields()
        self.update_json_data(json_data_fields)
        super().save(*args, **kwargs)

    def get_dynamic_fields(self):
        """
        Retrieve dynamic fields based on the fieldsets defined in the admin.
        """
        from .admin import DynamicFieldsModelAdmin
        fieldsets = DynamicFieldsModelAdmin(self._meta.model).get_fieldsets(None)
        json_data_fields = []
        for fieldset in fieldsets:
            if fieldset[0] == 'JSON Data':
                json_data_fields.extend(fieldset[1]['fields'])
        return json_data_fields
    
class JsonFieldDefinition(models.Model):
    """
    Model to store JSON field definitions.
    """
    json_dt = models.JSONField(default=dict)
