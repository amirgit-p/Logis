"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from root.sitemap import RootStaticUrl
from services.sitemap import ServicesStaticUrl , ServicesDynamicUrl

sitemaps = {
    'static-root': RootStaticUrl,
    'static-services': ServicesStaticUrl,
    'dynamic-services' : ServicesDynamicUrl,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("root.urls")),
    path("services/", include("services.urls")),
    path("accounts/",include("accounts.urls")),
    path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap",
),
    path('robots.txt', include('robots.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)