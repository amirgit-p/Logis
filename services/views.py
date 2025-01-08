from django.shortcuts import render, get_object_or_404
from .models import Services,Features , Options
from root.models import Testimonials,Fqa
from django.core.paginator import Paginator

def service (request , **kwargs):
    features = Features.objects.filter(status = True)
    tester = Testimonials.objects.filter(status = True)
    options = Options.objects.all()
    fqa = Fqa.objects.all()

    if kwargs.get("category"):
        services = Services.objects.filter(category__title=kwargs.get("category"), status=True)
    else:
        services = Services.objects.filter(status=True)
        

        


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
    category = Services.category

    context  = {
    "services" : services,
    "options" : options,
    "category": category,

    }

    return render(request , 'services/service-details.html',context=context)
