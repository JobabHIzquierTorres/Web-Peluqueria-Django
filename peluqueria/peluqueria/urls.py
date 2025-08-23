"""
URL configuration for peluqueria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from about.urls import about_patterns
from contact.urls import contact_patterns
from hours.urls import hours_patterns
from prices.urls import prices_patterns
from services.urls import services_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('about/', include(about_patterns)),
    path('contact/', include(contact_patterns)),
    path('hours/', include(hours_patterns)),
    path('prices/', include(prices_patterns)),
    path('services/', include(services_patterns)),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
