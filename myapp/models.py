from django.db import models

class Sections(models.Model):
    html = models.TextField()
    css = models.TextField()
    js = models.TextField()


class Villain(models.Model):
    name = models.CharField(max_length=255)
    is_unique = models.BooleanField(default=True)

    def __str__(self):
        return self.name