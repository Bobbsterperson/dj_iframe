from django.db import models


class JsonFieldDefinition(models.Model):
    json_field = models.JSONField()

class DynamicFieldsModel(models.Model):
    foreign_key_id = models.ForeignKey(JsonFieldDefinition, on_delete=models.CASCADE, related_name='dynamic_models')
    dynamic_data = models.JSONField()

