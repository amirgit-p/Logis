from django.shortcuts import render
from .models import Agent,Testimonials,Fqa,Contact,Quote , CountStars
from services.models import Services,Features, Options
from .forms import Contactform,Quoteform
from django.contrib import messages

def home(request):
    # services = Services.objects.filter(status = True)
    features = Features.objects.filter(status = True)
    tester = Testimonials.objects.filter(status = True)
    options = Options.objects.all()
    stars = CountStars.objects.all()
    fqa = Fqa.objects.all()

    if request.GET.get("search"):
        search = request.GET.get("search")
        services = Services.objects.filter(desc__contains=search, status = True)[:3] 
        
    else:
        services = Services.objects.filter(status = True)[:3] 

    context = {
        'services': services,
        'options' : options,
        'features': features,
        'tester':tester,
        'fqa': fqa,
        'stars' : stars,
    }
    return render (request, 'root/index.html',context=context)

def about(request):
    agents = Agent.objects.filter(status = True)
    fqa = Fqa.objects.all()
    tester = Testimonials.objects.filter(status = True)
    context = {
        'agents': agents,
        'tester':tester,
        'fqa': fqa,
    }
    return render (request, 'root/about.html',context=context) 

def contact(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.name = request.POST.get('name')
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            contact.save()
            messages.add_message(request,messages.SUCCESS,'success')
            return render (request, 'root/contact.html')
        else:
            messages.add_message(request,messages.ERROR,'not send')
            return render (request, 'root/contact.html')

    else:
        return render (request, 'root/contact.html')
    
def quote(request):
    if request.method == 'POST':
        quoteform = Quoteform(request.POST)
        if quoteform.is_valid():
            quote = Quote()
            quote.departure = request.POST.get('departure')
            quote.delivery = request.POST.get('delivery')
            quote.weight = request.POST.get('weight')
            quote.dimensions = request.POST.get('dimensions')
            quote.name = request.POST.get('name')
            quote.email = request.POST.get('email')
            quote.message = request.POST.get('message')
            quote.save()
            messages.add_message(request,messages.SUCCESS,'done sent')
            return render (request,'root/get-a-quote.html')
        else:
            messages.add_message(request,messages.ERROR,'not sent')
            return render (request,'root/get-a-quote.html')

    else:
        return render (request,'root/get-a-quote.html')