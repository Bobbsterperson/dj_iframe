from django.urls import path
from .views import toggle_bool_field_view


urlpatterns = [
    path('toggle-bool/<int:id>/', toggle_bool_field_view, name='toggle_bool_field'),
]
