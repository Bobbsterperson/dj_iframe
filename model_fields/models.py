from django.db import models
from ckeditor.fields import RichTextField

class AllFieldsModel(models.Model):
    # BooleanField
    bool_field = models.BooleanField(default=False)

    # JSONField
    json_data = models.JSONField()

    # NullBooleanField
    null_bool_field = models.BooleanField(null=True, blank=True)

    # CharField
    char_field = models.CharField(max_length=100)

    # TextField
    text_field = RichTextField(blank=True, null=True)

    # IntegerField
    int_field = models.IntegerField()

    # FloatField
    float_field = models.FloatField()

    # DecimalField
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)

    # DateField
    date_field = models.DateField()

    # DateTimeField
    datetime_field = models.DateTimeField()

    # TimeField
    time_field = models.TimeField()

    # EmailField
    email_field = models.EmailField()

    # URLField
    url_field = models.URLField()

    # UUIDField
    uuid_field = models.UUIDField()

    # FileField
    # file_field = models.FileField(upload_to='templates/', null=True, blank=True)

    # # ImageField
    # image_field = models.ImageField(upload_to='templates/', null=True, blank=True)


    def __str__(self):
        return self.char_field
