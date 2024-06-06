from django.contrib import admin
from .models import Sections
from django.http import HttpResponseRedirect
from .models import Villain

admin.site.register(Sections)

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    change_form_template = "admin/your_app/change_form.html"

    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(pk=obj.id)
            matching_names_except_this.delete()
            obj.is_unique = True
            obj.save()
            self.message_user(request, "This villain is now unique")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)