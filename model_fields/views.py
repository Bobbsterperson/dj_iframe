from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from model_fields.models import AllFieldsModel

def toggle_bool_field_view(request, id):
    try:
        instance = get_object_or_404(AllFieldsModel, id=id)
        instance.bool_field = not instance.bool_field  # Toggle the boolean field
        instance.save()
        return HttpResponse("Boolean field toggled successfully.")
    except Exception as e:
        return render(request, 'exception.html', {'exception': str(e)})
