from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from model_fields.models import AllFieldsModel
from django.core.exceptions import ValidationError

def toggle_bool_field_view(request, id):
    try:
        instance = get_object_or_404(AllFieldsModel, id=id)
        instance.bool_field = not instance.bool_field  # Toggle the boolean field
        instance.save()
        return HttpResponse("Boolean field toggled successfully.")
    except Exception as e:
        return render(request, 'exception.html', {'exception': str(e)})

def create_instance(request):
    try:
        instance = AllFieldsModel.objects.create(
            bool_field=True,
            char_field="Example",
            text_field="Example text",
            int_field=42,
            float_field=3.14,
            decimal_field=123.45,
            date_field="2024-07-10",
            datetime_field="2024-07-10T12:00:00Z",
            time_field="12:00:00",
            email_field="example@example.com",
            url_field="https://example.com",
            uuid_field="550e8400-e29b-41d4-a716-446655440000",
            file_field="path/to/uploaded_file.txt",
            image_field="path/to/uploaded_image.jpg",
            json_data={"key": "value"}
        )
        instance.save()
        return HttpResponse("Instance saved successfully!")
    except ValidationError as e:
        return HttpResponse(f"Validation error: {e}")
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}")

def show_instances(request):
    instances = AllFieldsModel.objects.all()
    return render(request, 'templates/instance_list.html', {'instances': instances})