from django.shortcuts import render

def services (request):
    return render(request , 'services/services.html')

def service_dtail (request):
    return render(request , 'services/service-dtail.html')
