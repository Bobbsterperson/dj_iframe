from django.contrib import admin
from .models import sections

@admin.register(sections)
class sectionsAdmin(admin.ModelAdmin):
    list_display = ('html', 'css', 'js')
