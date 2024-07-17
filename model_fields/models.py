from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
import os
import json

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
    datetime_field = models.DateTimeField(null=True, blank=True)
    time_field = models.TimeField(null=True, blank=True)
    url_field = models.URLField(null=True, blank=True)
    uuid_field = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=15, blank=True, default='')
    file = models.FileField(upload_to='files/', null=True, blank=True)

    def save(self, *args, **kwargs):
        original_json_data = self.json_data
        if self.file:
            file_path = os.path.join(settings.MEDIA_URL, self.file.name)
            file_name = os.path.basename(self.file.name)
            new_json_data = {
                'name': {'first_name': self.name.split()[0], 'last_name': ' '.join(self.name.split()[1:])},
                'email': self.email,
                'phone': self.phone,
                'file': {file_name: file_path},
            }
        else:
            new_json_data = {
                'name': {'first_name': self.name.split()[0], 'last_name': ' '.join(self.name.split()[1:])},
                'email': self.email,
                'phone': self.phone,
                'file': original_json_data.get('file', {}) if original_json_data else {},
            }
        if new_json_data != original_json_data:
            self.json_data = new_json_data
        super().save(*args, **kwargs)
