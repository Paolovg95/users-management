"""customUsers URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from users.views import restricted_page
from licitaciones import views as lic_views
from ofertas import views as offer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restricted/', restricted_page),
    path('licitaciones/', lic_views.view_all_licitaciones),
    path('licitaciones/mi-lista/', lic_views.view_my_licitaciones ),
    path('licitacion/<int:id>/', lic_views.view_licitacion, name='mi-licitacion'),
    path('ofertar/', offer_views.create_offer),
    path('accounts/', include('django.contrib.auth.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
