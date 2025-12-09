'''Api urls'''

from django.urls import path
from api.views import health_check

urlpatterns = [
    path('status/', health_check, name='health_check'),
]
