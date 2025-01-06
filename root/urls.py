from django.urls import path 
from .views import home , about , contact ,quote

app_name = 'root'

urlpatterns = [
    path("" , home , name='home' ),
    path("about" , about , name='about' ),
    path("contact" , contact , name='contactus' ),
    path('quote',quote,name='quote')
]

