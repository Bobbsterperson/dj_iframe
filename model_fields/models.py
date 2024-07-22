from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime, date, time

class AllFieldsModel(models.Model):
    bool_field = models.BooleanField(default=False)
    json_data = models.JSONField(default=dict)
    null_bool_field = models.BooleanField(null=True, blank=True)
    char_field = models.CharField(max_length=100, null=True, blank=True)
    text_field = RichTextField(blank=True, null=True)
    int_field = models.IntegerField(null=True, blank=True)
    float_field = models.FloatField(null=True, blank=True)
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_field = models.DateField(null=True, blank=True)
    time_field = models.TimeField(null=True, blank=True)
    url_field = models.URLField(null=True, blank=True)
    uuid_field = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=15, blank=True, default='')
    file = models.FileField(upload_to='files/', null=True, blank=True)
    twowordpoem = models.IntegerField(null=True, blank=True)
    datetime_field = models.DateTimeField(null=True, blank=True)

    def update_json_data(self, fields):
        self.json_data = {}
        for field in fields:
            value = getattr(self, field)
            if isinstance(value, models.fields.files.FieldFile):
                self.json_data[field] = value.url if value else ''
            elif isinstance(value, (datetime, date, time)):
                self.json_data[field] = value.isoformat() if value else ''
            else:
                self.json_data[field] = value
