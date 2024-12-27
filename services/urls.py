from django.urls import path 
from .views import service,service_detail

app_name = 'services'

urlpatterns = [
    path("", service , name='services'),
    path('detail', service_detail , name='detail'),
]
