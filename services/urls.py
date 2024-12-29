from django.urls import path 
from .views import service,service_detail

app_name = 'services'

urlpatterns = [
    path("", service , name='services'),
    path("category/", service, name="services-category"),
    path('details/<int:id>', service_detail , name='service-details'),
]
