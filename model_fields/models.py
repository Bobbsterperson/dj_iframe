from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core import validators
from django.core.exceptions import ValidationError

class AllFieldsModel(models.Model):
    
    # BooleanField
    bool_field = models.BooleanField(default=False)

    # jsonfield
    # json_data = JSONField()
    # name = models.CharField(max_length=100)
    # phone = models.CharField(max_length=20)
    # mail = models.EmailField()
    # file = models.FileField(upload_to='files/')

    # json_data = JSONField(
    #     validators=[
    #         validators.RegexValidator(
    #             regex=r'^{"name": ".+", "phone": ".+", "mail": ".+", "file": ".+"}$',
    #         ),
    #     ]
    # )

    # NullBooleanField
    null_bool_field = models.BooleanField(null=True, blank=True)
    # CharField

    char_field = models.CharField(max_length=100)

    # TextField
    text_field = models.TextField()

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
    file_field = models.FileField(upload_to='uploads/')

    # ImageField
    image_field = models.ImageField(upload_to='images/')

    # FilePathField
    file_path_field = models.FilePathField(path='/var/www/html/')

    # ForeignKey
    # Example linking to another model within the same app
    # Replace 'AnotherModel' with an actual model name in your project
    # another_model = models.ForeignKey('AnotherModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.char_field  # Or whatever makes sense as a string representation

