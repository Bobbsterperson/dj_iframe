from django.urls import path
from .views import toggle_bool_field_view
from .views import create_instance

urlpatterns = [
    path('toggle-bool/<int:id>/', toggle_bool_field_view, name='toggle_bool_field'),
    # path('create-instance/', create_instance, name='create_instance'),
]
