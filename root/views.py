from django.shortcuts import render
from .models import Agent,Testimonials,Fqa
from services.models import Services,Features
def home(request):
    services = Services.objects.filter(status = True)
    features = Features.objects.filter(status = True)
    tester = Testimonials.objects.filter(status = True)
    fqa = Fqa.objects.all()
    context = {
        'services': services,
        'features': features,
        'tester':tester,
        'fqa': fqa,
    }
    return render (request, 'root/index.html',context=context)

def about(request):
    agent = Agent.objects.filter(status = True)
    fqa = Fqa.objects.all()
    tester = Testimonials.objects.filter(status = True)
    context = {
        'agent': agent,
        'tester':tester,
        'fqa': fqa,
    }
    return render (request, 'root/about.html',context=context) 

def contact(request):
    return render (request, 'root/contact.html')