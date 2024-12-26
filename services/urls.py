from django.urls import path 
from .views import services , service_dtail 

app_name = 'services'

urlpatterns = [
    path("service", services , name='services'),
    path('dtail', service_dtail , name='service_detail'),
]
