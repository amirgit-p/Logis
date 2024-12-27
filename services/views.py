from django.shortcuts import render
from .models import Services_details,Services,Features
from root.models import Testimonials,Fqa

def service (request):
    services = Services.objects.filter(status = True)
    features = Features.objects.filter(status = True)
    tester = Testimonials.objects.filter(status = True)
    fqa = Fqa.objects.all()
    context = {
        services: 'services',
        features: 'features',
        tester: 'tester',
        fqa: 'fqa',
    }

    return render(request , 'services/services.html',context=context)

def service_detail (request):
    service = Services_details.objects.filter(default=True)
    context  = {
    service :'service',
    }
    return render(request , 'services/service-dtail.html',context=context)
