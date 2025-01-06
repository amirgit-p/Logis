from django.shortcuts import render, get_object_or_404
from .models import Services,Features , Options
from root.models import Testimonials,Fqa
from django.core.paginator import Paginator

def service (request):
    services = Services.objects.filter(status = True)
    features = Features.objects.filter(status = True)
    tester = Testimonials.objects.filter(status = True)
    options = Options.objects.all()
    fqa = Fqa.objects.all()

    services_paginate = Paginator(services, 3)
    first_page = 1
    last_page = services_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        services = services_paginate.get_page(page_number)
    except:
        page_number = first_page
        services = services_paginate.get_page(first_page)

    context = {
        "services" : services,
        "features" : features,
        "tester" : tester,
        "fqa" : fqa,
        "options" : options,
        "first" : first_page,
        "last" : last_page,
    }

    return render(request , 'services/services.html',context=context)

def service_detail (request, id):
    services = get_object_or_404(Services, id=id)
    options = Options.objects.all()

    context  = {
    "services" : services,
    "options" : options,
    }

    return render(request , 'services/service-details.html',context=context)
