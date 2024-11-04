"""
URL configuration for TechStackPortfolio project.

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
import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path('', include('main_portfolio_presentation_cv.urls')),
    path('inventory_management_system/', include('inventory_management_system.urls')),
    path('to_do_list_app', include('to_do_list_app.urls')),
    path('login/', views.crispy_login_view, name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('register/', views.crispy_register_view, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
