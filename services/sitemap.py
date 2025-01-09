from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Services

class ServicesStaticUrl(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def items(self):
        return [
            "services:services",
        ]  
    def location(self, item):
        return reverse(item)

class ServicesDynamicUrl(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def items(self):
        return Services.objects.all()
     
    def location(self, item):
        return "/services/details/%i"%item.id
 