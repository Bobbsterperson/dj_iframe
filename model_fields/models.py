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
    char_field = models.CharField(max_length=100, null=True, blank=True)

    # TextField
    text_field = RichTextField(blank=True, null=True)

    # IntegerField
    int_field = models.IntegerField(null=True, blank=True)

    # FloatField
    float_field = models.FloatField(null=True, blank=True)

    # DecimalField
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # DateField
    date_field = models.DateField(null=True, blank=True)

    # DateTimeField
    datetime_field = models.DateTimeField(null=True, blank=True)

    # TimeField
    time_field = models.TimeField(null=True, blank=True)

    # EmailField
    email_field = models.EmailField(null=True, blank=True)

    # URLField
    url_field = models.URLField(null=True, blank=True)

    # UUIDField
    uuid_field = models.UUIDField(null=True, blank=True)

    # FileFieldtxt
    file_field = models.FileField(upload_to='templates/', null=True, blank=True)

    # ImageField
    image_field = models.ImageField(upload_to='templates/', null=True, blank=True)


    def __str__(self):
        return self.char_field
