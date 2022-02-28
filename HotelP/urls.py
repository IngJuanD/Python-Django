"""HotelP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from HotelLP.views import contacto, habitaciones, inicio, planes, registro, reserva
from django.conf.urls.static  import static
from HotelP.settings import MEDIA_ROOT, MEDIA_URL



#agregar las paginas
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('inicio/',inicio),
    path ('reserva/',reserva),
    path ('habitaciones/',habitaciones),
    path ('planes/',planes),
    path ('registro/',registro),
    path ('contacto/',contacto),
    path('accounts/',include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)