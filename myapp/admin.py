from django.contrib import admin
from .models import Sections
from django.http import HttpResponseRedirect
from .models import Sections

@admin.register(Sections)
class CodeSnippetAdmin(admin.ModelAdmin):
    change_form_template = "admin/myapp/change_form.html"

    def save_model(self, request, obj, form, change):
        obj.html = form.cleaned_data['html']
        obj.css = form.cleaned_data['css']
        obj.js = form.cleaned_data['js']
        super().save_model(request, obj, form, change)