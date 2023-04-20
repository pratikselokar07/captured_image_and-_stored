from django.urls import path
from .views import camera

urlpatterns = [
    path('camera/', camera, name='camera'),
]